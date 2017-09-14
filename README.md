


<div align="center">
<h1>CSV2YAML</h1>
	
<p>Convert CSV File To JSON, YAML & Pickle	</p>

</div>	
	
	

----------		

		


<div align="center">
<a href="https://codecov.io/gh/sepandhaghighi/csv2yaml">
  <img src="https://codecov.io/gh/sepandhaghighi/csv2yaml/branch/master/graph/badge.svg" alt="Codecov" />
</a>
<a href="https://www.codacy.com/app/sepand-haghighi/csv2yaml?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sepandhaghighi/csv2yaml&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/7a8c9902f6354a9b910ca22e35d785a2"/></a>
<a href="https://badge.fury.io/py/csv2yaml"><img src="https://badge.fury.io/py/csv2yaml.svg" alt="PyPI version" height="18"></a>
</div>



	


	
</hr>
</hr>

## Installation
### Source Code
- Download [Version 0.1](https://github.com/sepandhaghighi/csv2yaml/archive/v0.1.zip) or [Latest Source ](https://github.com/sepandhaghighi/csv2yaml/archive/master.zip)
- `pip3 install -r requirements.txt` or `pip install -r requirements.txt` (Need root access)	 
- `python3 setup.py install` or `python setup.py install`	


### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install csv2yaml` or `pip3 install csv2yaml` (Need root access)					
					
			

## Usage			
				

### Command Line

- Run csv2yaml with file as argument `python3 -m csv2yaml file.csv header_optional` or `python -m csv2yaml file.csv header_optional` on Mac,Linux or Windows
- Default Header : Filename


<div align="center">
<img src="csv2yaml_usage.gif" alt="csv2yaml usage" title="csv2yaml usage">
</div>
						
				
## Automated Build				


<div align="center">
<table align="center" style="border:1px solid black;">
<tr>
<th>Linux</th>
<th>Windows</th>

</tr>

<tr>
<td><a href="https://travis-ci.org/sepandhaghighi/csv2yaml"><img src="https://travis-ci.org/sepandhaghighi/csv2yaml.svg?branch=master"></a></td>
<td> <a href="https://ci.appveyor.com/project/sepandhaghighi/csv2yaml"><img src="https://ci.appveyor.com/api/projects/status/4jvejgwe53nnaq3k?svg=true"></a></td>

</tr>	

</table>

</div>	

## Input File Format

```
	Key1,Key2,...,KeyN
	Value11,Value12,...,Value1N
	.
	.
	.
	ValueN1,ValueN2,...,ValueNN
```
		
## Output File Format

- [JSON(.json)](https://en.wikipedia.org/wiki/JSON)

	```
		{
		"header_name": {
				"data":[
				{
					"id"  : "1",
					"Key1": "Value11",
					"Key2": "Value12",
					.
					.
					.
					"KeyN": "Value1N"
				},

				.
				.
				.

				{
					"id"  : "N",
					"Key1": "ValueN1",
					"Key2": "ValueN2",
					.
					.
					.
					"KeyN": "ValueNN"
				},
				]
			}
		}
	```

- [YAML(.yaml)](https://en.wikipedia.org/wiki/YAML)
	```
		header_name:
  			data:
			- Key1: "Value11"
    	  	Key2: "Value12"
    	  	.
            .
            .
			KeyN: "Value1N"
			id  : "1"
		
			.
			.
			.

			- Key1: "ValueN1"
    	  	Key2: "ValueN2"
    	  	.
            .
            .
			KeyN: "ValueNN"
			id  : "N"

	``` 

- [Pickle(.p)](https://docs.python.org/3.5/library/pickle.html) (Binary Format)													
## TODO		

- [x] Formats
  - [x] JSON
  - [x] YAML
  - [x] Pickle
			

## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!							
or send an email to [sepand@qpage.ir](mailto:sepand@qpage.ir "sepand@qpage.ir"). 


## Contribution			

You can fork the repository, improve or fix some part of it and then send the pull requests back if you want to see them here. I really appreciate that. ❤️			

Remember to write a few tests for your code before sending pull requests. 
					
## Donate to our project									

If you feel like our project is important can you please support us?			
Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do.

<h3>Bitcoin :</h3>					

```1XGr9qbZjBpUQJJSB6WtgBQbDTgrhPLPA```
				

<h3>Payping (For Iranian citizens) :</h3>

<a href="http://www.payping.net/sepandhaghighi" target="__blank"><img src="http://www.qpage.ir/images/payping.png" height=100px width=100px></a>

## License
<div align="center">
<a href="https://github.com/sepandhaghighi/csv2yaml/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mashape/apistatus.svg"/></a>
</div>



			

