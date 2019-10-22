# crapy-doctors
Scrape de Clinicas

python3 -m venv .venv

pip install -r requirements.txt

scrapy runspider doctoralia.py -s HTTPCACHE_ENABLE=1 -s CLOSESPIDER_ITEMCOUNT=500 -o doctors.csv

# busca especialidades 
``` 
scrapy shell https://www.doctoralia.com.br/especializacoes-medicas/
response.xpath("//div[@class='display-flex justify-content-between align-items-center']//a[@class='text-muted']//@href").getall()
``` 

# busca especialidades por cidades
```  
scrapy shell https://www.doctoralia.com.br/especializacoes-medicas/em-detalhe/urologista
response.xpath("//ul[@class='list-unstyled row']//a//@href").getall()
``` 

# busca  lista de medicos por cidade
``` 
scrapy shell https://www.doctoralia.com.br/urologista/sorocaba
response.xpath("//ul[@class='search-list list-unstyled']//a//@href").getall() 
``` 

