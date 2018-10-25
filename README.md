## HideBox
Escrito em python2, HideBox é que criptografa e oculta um arquivo em uma imagem png.

O script é uma implementação do Stepic.
## Sintaxe
```sh 
Usage: hidebox.py [-e] -i IMAGE -f FILE

HideBox - Oculta arquivos em imagens de forma segura.

Options:
  --version            show program's version number and exit
  -h, --help           show this help message and exit
  -e, --encode         Modo de criptografar e codificar dado na imagem
                       apontada.
  -d, --decode         Modo de descriptografar e decodificar o dado na imagem
                       apontada
  -i IMAGE             IMAGE alvo que recebera o FILE
  -f FILE              FILE alvo que sera codificado na IMAGE.
  -c CRYPT             criptografia que sera usada
  --list-crypt         criptografia que sera usada
  -o FILE, --out=FILE  Escreve os dados obtidos de IMAGE no arquivo FILEOUT.
  ```
## Implementação de criptografia
- O arquivo necessita de 2 funções, main_encrypt e main_decrypt
- É preciso estar na pasta lib
