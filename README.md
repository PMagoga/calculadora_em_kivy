## calculadora_em_kivy

Uma calculadora usando o Framework *Kivy*, tentei adicionar o arquivo para Android aqui, mas ele passou dos 25 MB, então vou mostrar aqui o passo a passo para que você possa fazer isso no seu computador e ainda treinar um pouco a usar o Kivy, basta você clonar o código para seu editor favorito e digitar os seguintes comando no terminal.

## Se você não quiser ter o **prazer** de transformar o arquivo para Android você mesmo, vou deixar o link do [Google Drive](https://drive.google.com/file/d/1gdXdRKWNmyNxq2S3683MU_UuCiU9Oavk/view?usp=sharing) para você baixar o arquivo direto para o seu celular e testar a calculadora.

### instalar o pacote chamado buildozer com o pip:
$ pip install buildozer

### feita a instalação do pacote, digite o seguinte comando:
$ buildozer init

vai criar um chamado buildozer.spec, após isso, verifique se todas as dependências do buildozer são cumpridas para o seu sistema operacional, você pode verificar isso clicando nesse link [buildozer](https://buildozer.readthedocs.io/en/latest/installation.html#targeting-android).

### Agora a última etapa para criar o aplicativo é digitar o comando: 

ahhhh pera, antes de digitar o comando abaixo, esqueci de dizer, é imprescindível que você renomeie ou crie uma cópia do seu arquivo com o código, e de a ele o nome de **main.py**, senão o buildozer não vai funcionar.

### Agora sim, tudo pronto, digite o seguinte comando:
$ buildozer -v android debug

essa etapa leva muito tempo! Sério, muito tempo mesmo, claro eu to levando em consideração a minha máquina que é bem fraquinha, levou uns 25 minutos, talvez na sua demore bem menos, tipo uns 22 minutos.

Se tudo correr conforme o planejado, você terá um arquivo com um nome parecido *kvcalc-0.1-debug.apk* na pasta do seu projeto.

Então é só conectar um cabo usb no seu celular, copiar o arquivo *kvcalc-0.1-debug.apk* clicar no arquivo e fazer a instalar e voilá.
