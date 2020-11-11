/*
 * ArduinoLicht.c
 *
 * Created: 09/11/2020 17:29:41
 * Author : Sabine
 * Deze code werkt alleen autonoom en is nog niet getest met GUI.
 */ 


#include "AVR_TTC_scheduler.h"
#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#define F_CPU 16E6
#include <util/delay.h>
#include <avr/eeprom.h>
#define UBBRVAL 51

volatile uint8_t status = 0x01;
volatile uint8_t min_uitrol = 5;
volatile uint8_t max_uitrol = 160;
volatile uint8_t uitrol = 0;
volatile uint8_t max_licht = 25;
volatile uint8_t lichtintensiteit = 0;
volatile uint8_t adcValue = 0;
volatile uint8_t isBusy = 0;
volatile uint8_t isRolling = 0;
//volatile uint8_t pulse = 0; // wordt alleen gebruikt voor ultrasoon sensor
//volatile int16_t COUNTB = 0; //wordt alleen gebruikt voor ultrasoon sensor


void setup() {
	DDRD = 0xFF; // pin 2,3,4
	DDRB = 0xFF; // wordt niet gebruikt
}

// Zet de waarden voor de serieele verbinding
// Dit komt uit de datasheet
void uart_init(){
	UBRR0H = 0;
	UBRR0L = UBBRVAL;
	UCSR0A = 0;
	UCSR0B = _BV(TXEN0) | _BV(RXEN0);
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
}

// Verstuur data
void transmit(uint8_t data){
	loop_until_bit_is_set(UCSR0A, UDRE0);
	UDR0 = data;
}

// Ontvang data
uint8_t receive(void) {
	loop_until_bit_is_set(UCSR0A, RXC0);
	return UDR0;
}

/*
ADMUX is the ADC multiplexer selection register (register that contains three fields of bits for 
controlling various aspects of data conversion)
ADCSRA is the ADC control and status register A

ADPS0 = 0 (ADC Prescaler select bits)
ADPS1 = 1 (ADC Prescaler select bits)
ADPS2 = 2 (ADC Prescaler select bits)
*/
void adc_init(){
	   ADCSRA |= (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0); // Zet de ADC prescalar op 128
	   ADMUX |= (1 << REFS0); // Zet ADC reference naar AVCC
	   ADCSRA |= (1 << ADEN);  // Zet ADC aan
   }
   
// Param: uit te lezen poort
// Return: de digitale waarde
int readAdc(uint16_t port){
	ADMUX = 0xf0; //voor MUX3-0 op 0 zetten
	ADMUX |= port; //OR om desbetreffende poort op 1 zetten (bijv als param 1 was zet A1 op 1)
	
	uint8_t value;
	// ADCSRA is control and status register A
	// setting ADSC to 1 initiates a single conversion (bit 6)
	ADCSRA |= (1<<ADSC); // 0000 0001 << 6 results in 0100 0000, 6e bit op 1 = start conversion
	while(ADCSRA & (1<<ADSC)){};
	value = ADCH;
	return value;
}
   
void set_eeprom_address(){
	eeprom_write_byte(0x00, 0x01); // Geef aan dat er data is
	eeprom_write_byte(0x01, status);
	eeprom_write_byte(0x02, min_uitrol);
	eeprom_write_byte(0x03, max_uitrol);
	eeprom_write_byte(0x04, uitrol);
	eeprom_write_byte(0x05, max_licht);
	eeprom_write_byte(0x06, lichtintensiteit);
   }
   
void get_eeprom(){
	status = eeprom_read_byte(0x01);
	min_uitrol = eeprom_read_byte(0x02);
	max_uitrol = eeprom_read_byte(0x03);
	uitrol = eeprom_read_byte(0x04);
	max_licht = eeprom_read_byte(0x05);
	lichtintensiteit = eeprom_read_byte(0x06);
   }

// De rode LED aanzetten op Poort D pin 3 ( 8 = 0000 1000)
void RoodLEDaan(){
	PORTD |= 8; //0000 0000 0000 1000 |= 0000 0000 0000 0000
}

// De rode LED aanzetten op Poort D pin 3 ( 8 = 0000 1000)
void RoodLEDuit(){
	PORTD &=~ 8;
}

// De groene LED gaat aan op poort D pin 2 (4 = 0000 0100)
void GroenLEDaan(){
	PORTD |= 4;
}

// De groene LED gaat uit op poort D pin 2 (4 = 0000 0100)
void GroenLEDuit(){
	PORTD &=~ 4;
}

// De gele LED gaat aan op poort D pin 4 ( 16 = 0001 0000)
void GeelLEDaan(){
	PORTD |= 16;
}

// De gele LED gaat uit op poort D pin 4 ( 16 = 0001 0000)
void GeelLEDuit(){
	PORTD &=~ 16;
}

// Bereken de lichtintensiteit
void tempsensor(void){
	lichtintensiteit = readAdc(0);
	_delay_ms(10);
}

// Laat de rode LED branden en de gele LED knipperen
void schermoprollen(){
	isRolling = 1;
	if(PORTD == 0x04) { // check of groen nog aan staat, zo ja zet hem uit
		GroenLEDuit();
	}
	RoodLEDaan();
		while(uitrol > min_uitrol){
			GeelLEDaan();
			_delay_ms(500);
			GeelLEDuit();
			_delay_ms(500);
			if(uitrol - 10 < min_uitrol){
				uitrol -= uitrol - min_uitrol;
				eeprom_write_byte(0x04, uitrol);
			}else{
				uitrol -= 10;
				eeprom_write_byte(0x04, uitrol);
			}
		}
	isRolling = 0;
}

// Laat de groene LED branden en de gele LED knipperen
void schermuitrollen(){
	isRolling = 1;
	if(PORTD == 0x08 ) { // check of rood nog aan staat, zo ja zet hem uit
		RoodLEDuit();
	}
	GroenLEDaan();
		while(uitrol < max_uitrol) {
			GeelLEDaan();
			_delay_ms(500);
			GeelLEDuit();
			_delay_ms(500);
			if(uitrol + 10 > max_uitrol){
				uitrol += max_uitrol - uitrol;
				eeprom_write_byte(0x04, uitrol);
			}
			else{
				uitrol += 10;
				eeprom_write_byte(0x04, uitrol);
			}
		}	
	isRolling = 0;
}

/* WE HEBBEN GEEN ULTRASOON SENSOR
// Bereken de afstand aan de hand van de ultrasoon sensor
void getDistance(void){
	COUNTB = 0;
		//pulse van naar de trigger
		PORTB|=(1<<PORTB0);
		_delay_us(10);
		PORTB &=~(1<<PORTB0);

		COUNTB = 0;
		
		// Als echo 0 terug stuurt doe niks
		while((PINB & (1<<PINB1)) == 0x00){}
		
		// Als echo niet 0 is +1 bij COUNTB
		while((PINB & (1<<PINB1)) != 0x00){
			COUNTB += 1;
		}
		
		// De duration van een echo / 58 is afstand
		pulse = COUNTB / 58;

		_delay_ms(1000);
	}
*/

// Rol het scherm automatisch in of uit
void rol(){
	if((status == 1) & (isRolling == 0)){
		if(lichtintensiteit > max_licht){
			schermuitrollen(); // Groen
		}else{
			schermoprollen(); // Rood
		}		
	}
}

void run(void){
	if(isBusy == 0){
		uint8_t data = receive();
		// Verstuur het type eenheid
		if(data == 0xff){
			transmit(0xd0); // Lichtsensor
		}
		
		// Verstuur de status
		if(data == 0x10){
			transmit(status);  // 0= handmatig, 1= autonoom
		}
		
		//  Zet de status op handmatig
		if(data == 0x20){
			status = 0x00; // handmatig
			eeprom_write_byte(0x01, status);
		}
		
		// Zet de status op autonoom
		if(data == 0x30){
			status = 0x01; // autonoom
			eeprom_write_byte(0x01, status);
		}
		
		// Uitrollen
		if(data == 0x40){
			schermuitrollen(); // zet uitrol naar de current uitrolafstand, schrijf dit naar eeprom (0x04)
			//transmit(uitrol) // stuur data terug?
		}
		
		// Oprollen
		if(data == 0x50){
			schermoprollen(); // zet uitrol naar de current uitrolafstand, schrijf dit naar eeprom (0x04)
			//transmit(uitrol)// stuur data terug?
		}
		
		// Stuur huidige min en max uitrol
		if(data == 0x60){
			transmit(min_uitrol);
			transmit(max_uitrol);
		}
		
		// Stuur huidige max licht
		if(data == 0x70){
			transmit(max_licht);
		}
		
		// Stel de maximale uitrol in
		if(data == 0x80){
			isBusy = 1;
			max_uitrol = receive();
			eeprom_write_byte(0x03, max_uitrol);
			isBusy = 0;
		}
		
		// Stel de minimale uitrol in
		if(data == 0x81){
			isBusy = 1;
			min_uitrol = receive();
			eeprom_write_byte(0x02, min_uitrol);
			isBusy = 0;
		}
		
		// Stel de lichtintensiteit in waarbij uitgerold moet worden
		if(data == 0x82){
			isBusy = 1;
			max_licht = receive();
			eeprom_write_byte(0x05, max_licht);
			isBusy = 0;
		}
		
		// Verstuur de temperatuur
		if(data == 0xa0){
			transmit(lichtintensiteit);
		}
		
		// verstuur de uitrol (hoe ver het scherm op het moment is uitgerold)
		if(data == 0xb0){
			transmit(uitrol);
		}
		
		// Verstuur de lichtintensiteit en huidige maximale licht om uit te rollen
		if(data == 0xc0){
			transmit(lichtintensiteit);
			transmit(max_licht);
		}
	}
}

int main(void){
	if(eeprom_read_byte(0x00) != 0x01){ // check of er nog geen data is
		set_eeprom_address(); //vul EEPROM met de volatile variabelen
	}
	else{
		get_eeprom(); //als er al wel waarden waren, haal ze op en zet ze in de volatile variabelen
	}
	
	// Set up de ports
	setup();
	
	// Initialise communicatie en ADC
	uart_init();
	adc_init();
	
	//tests
	//if lichtintensiteit>max_licht: schermuitrollen
	//schermuitrollen == Green
	//schermoprollen == Red
	isRolling=0;
	status=1;
	max_licht = 100;
	lichtintensiteit = 200;
	
	SCH_Init_T1(); // Initialise de timer, default 10ms
	
	// Voeg tasks toe aan de scheduler
	//SCH_Add_Task(run, 0, 1);
	SCH_Add_Task(tempsensor,1000, 1000); 
	//SCH_Add_Task(getDistance,1200,1000); // Ultrasoon sensor niet geimplementeerd
	SCH_Add_Task(rol,500,3000); // tijd verkort voor testing purposes
	
	SCH_Start(); // De scheduler starten
	
	while(1){
		SCH_Dispatch_Tasks();
	}
}