# Web-scraping-wmb

Esse e um código que faz a rapagem do site 'https://branham.org/pt/MessageAudio' <br>
esse código analisa o site e e pega todos os sermões e gera um aquivo 'sermons.json' <br>
com uma lista contendo o titulo, detalhes, link do download do audio e o link de download do pdf.
<br><br>
## exemplo do arquivo sermons.json

```javascript
[
  {
  "title": "A Deidade de Jesus Cristo",
  "datails": "POR 49-1225",
  "audio": "https://s3.amazonaws.com/omega-public-audio/repo/5bb/5bbfa1e1ba04f71dadd9d1d55ff79873964c78246d85b178ee3ede7c7e148d87cd0bc4c122ec24ce1c408cca803868c1b1bd403bcafb1e0ce96682005aac9b93.m4a",
  "pdf": "https://s3.amazonaws.com/omega-public-text/repo/b39/b39fb67e096efb1a8a15c4d0af31e7c04989ff7f62709175f6832cfb80d88b2fbd82bf3aa2a1522cee8d579872a1ed1b2da15da912802322c72565b9244e7524.pdf"
  },
  {
    "title": "Doenças e Aflições",
    "datails": "POR 50-0100",
    "audio": "https://s3.amazonaws.com/omega-public-audio/repo/24c/24c1e3bbdc9f95b08ba735ddfbb19f6a4b6ea7efc7e94e16e02413255930d13026a5e159f0968f0b55888ead4c700ecc061976f7a282edf631449ba29fa283cb.m4a",
    "pdf": "https://s3.amazonaws.com/omega-public-text/repo/aba/aba7ec6ea77f8e1b7e13d3c5fc0e0e237841cd87765fedb54e40786e636066dfdbfc1adfe53e65484b5eded1b8cf64f46baafe352fa59df6ef3ac8d6ea3f03f6.pdf"
  }
]
```

## executar o código

- Tenha o python3 instalado na maquina.

- Na raiz do projeto execute:
```terminal
python -m pip install -r requirements.txt
```
- Apos o comando anterior terminar execute:
```terminal
python3 -i code/scraper.py
```

- Na raiz do projeto sera gerado um arquivo 'sermons.json' contendo as informações do site.

- Com arquivo gerado aberto no VsCode pressione ctrl + s para formatar o arquivo.