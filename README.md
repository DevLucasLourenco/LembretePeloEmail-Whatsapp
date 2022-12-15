# LembretePeloEmail-Whatsapp
Criei esse código para uso pessoal, onde o seu objetivo era enviar uma mensagem no whatsapp e um email para a pessoa destinada não esquecer de tomar seu remédio. Após a conclusão de sua funcionalidade, decidi trazer este código para o meu Github para usos futuros.


## Explicação do código

Como dito anteriormente, criei esse código para uso pessoal.
Após ele ter concluído o que eu queria, que era avisar a devida pessoa a hora de tomar seu remédio, decidi modificá-lo um pouco e trazer para o github.

Durante sua criação, visei fazer com que suas principais ações estivessem em ```def functions```. Tal como o ```envio do email``` e o ```envio da mensagem no whatsapp```


Mas, antes mesmo disso ser possível, desenvolvi uma function onde seu nome era ```conexão```. Ela era responsável por realizar o login do whatsapp através do QR Code.

Ao mesmo tempo, criei outras functions para a melhor compreenção do código e a integridade do mesmo. Elas são: ```adaptar_item()``` e ```hora_setup()```


Também criei um arquivo ```.txt```, para fazer com que eu não precisasse rodar o código 24h/dia, afinal, através desse arquivo .txt, ele iria salvar qual era dose que a pessoa deveria tomar,
fazendo então com que não se perdesse essa informação ao reiniciar o computador ou executar o código novamente.


E, por fim, o principal do programa era que, ao chegar a hora de tomar a dosagem, ele enviasse as mensagens.

Usei bibliotecas para a realização disso e foi feito. Sempre que era chego o horário de tomar, tudo funcionava. Enquanto não chegava a hora, ele aguardava.
