# GS_IOT

### Explicação do Projeto: Sistema de Alerta por Gestos em Apagões

Visão Geral
Nosso projeto apresenta uma solução tecnológica para comunicação em situações de falta de energia, utilizando visão computacional e inteligência artificial para reconhecer gestos humanos como forma de pedido de ajuda. O sistema foi desenvolvido para operar mesmo em condições de baixa luminosidade, sendo especialmente útil durante emergências causadas por apagões.

Como Funciona?

Detecção de Gestos (Python + MediaPipe)
Utilizamos a biblioteca MediaPipe para identificar mãos e dedos em tempo real, capturando posições e movimentos específicos. O sistema reconhece três gestos de emergência principais:

Mão aberta repetida três vezes: aciona luzes de emergência

Polegar para cima com movimento lateral: envia alerta silencioso para equipes

Formação de "SOS" com os dedos: dispara notificação para sistemas de monitoramento

Processamento de Imagem (OpenCV)
Implementamos algoritmos de processamento de imagem adaptados para ambientes escuros, incluindo:

Ajuste automático de contraste

Realce de bordas

Detecção de movimento

Sistema de Alertas
Quando um gesto é identificado, o sistema:

Ativa luzes LED (simuladas via interface)

Emite alertas sonoros personalizados

Exibe notificações no painel de controle

Diferenciais Tecnológicos

Funcionamento offline, sem dependência de internet

Baixo custo de implementação, rodando em hardware convencional

Solução acessível, com gestos intuitivos e interface simplificada

Aplicações Práticas

Hospitais: comunicação silenciosa em salas cirúrgicas durante falhas de energia

Indústrias: sistema de SOS em áreas de risco sem iluminação

Residências: auxílio para idosos e pessoas com deficiência visual
