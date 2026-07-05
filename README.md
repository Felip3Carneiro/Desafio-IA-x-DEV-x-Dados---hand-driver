# Desafio IA x DEV x Dados hand-driver

# Controle de Jogo com IA e Reconhecimento de Gestos

**Projeto** para o **Hands-on** da **Carreira Tech FIAP** "Inteligência Artificial, DEV e Dados: Como o Futuro Está Sendo Programado"

---

Desenvolvido por: Felipe Cardoso Vilar Carneiro

---

## Objetivo

Criar uma integração entre Inteligência Artificial e um jogo, permitindo controlar ações usando apenas movimentos da mão capturados pela webcam.

---

## Como funciona

Fluxo do sistema:

Webcam → IA processa → Veredito → Comando → Jogo

1. A câmera captura os movimentos da mão do jogador;
2. A IA analisa os dados recebidos;
3. O modelo retorna um veredito (classe reconhecida + confiança);
4. O resultado é convertido em ações;
5. O PgZero aplica essas ações no jogo.

---

## Ideia central

### Reconhecimento:

Exemplo:

Gesto detectado:
Classe: Like
Confiança: 96%

↓

Ação no jogo:
Mover carro →

---

## Tecnologias utilizadas

- Python
- OpenCV
- PgZero
- Modelo IA para reconhecimento de gestos(https://teachablemachine.withgoogle.com)
- Webcam

---

## Comandos reconhecidos

| Gesto | Ação | Label
|------|------|------|
| Like | Move para direita | Like
| Dislike | Move para esquerda | Não like
| Mão aberta | Parar | Parar
| Outro | Segue a ação anterior até outra ser estabelecida | Nada

(Editar conforme seu projeto e modelo de I.A.)

---

## Resultados na prática

- Reconhecimento em tempo real

- Integração funcional com jogo

- Controle por gestos usando webcam

---

## ⚠️ Limitações

O reconhecimento pode variar dependendo de:

- iluminação;
- posição da mão;
- qualidade da webcam;
- gestos semelhantes;
- Cores de fundo;
- etc.

---

## 📷 Exemplo do sistema em funcionamento

<img width="1920" height="1080" alt="vlcsnap-2026-05-23-21h59m38s015" src="https://github.com/user-attachments/assets/5bb6583b-842a-4be0-b1ca-bad0ecedd29d" />

![Video daora](video\video.gif)

```

Acabou

