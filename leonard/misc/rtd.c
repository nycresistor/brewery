/*
 *  RTD Sensor Code
 */
 
#include <mraa.h>
#include <unistd.h>
#include <stdint.h>

int main(int argc, char **argv)
{
    mraa_init();
    mraa_spi_context spi;
    spi = mraa_spi_init(0);
    unsigned int response = 0;
    printf("Now Attempting to READ RTD Registers over SPI\n");
    uint8_t data = 0x00;
    uint8_t *recv;

    recv = mraa_spi_write_buf(spi, data, 2);
    printf("RECIVED-%i-%i\n",recv[0],recv[1]);

    recv = mraa_spi_write_buf(spi, data, 2);
    printf("RECIVED-%i-%i\n",recv[0],recv[1]);

    recv = mraa_spi_write_buf(spi, data, 2);
    printf("RECIVED-%i-%i\n",recv[0],recv[1]);

    recv = mraa_spi_write_buf(spi, data, 2);
    printf("RECIVED-%i-%i\n",recv[0],recv[1]);

}

