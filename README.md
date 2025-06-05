# GS_IOT

###Integrantes
integrantes do grupo

- Augusto Milreu rm 98245
- Fernando Popolili rm 99919
- Matheus Zanardi rm 98832

### Descrição do problema
O problema de interrupções no fornecimento de energia elétrica representa um desafio significativo para a sociedade moderna, afetando desde residências até infraestruturas críticas como hospitais e sistemas de segurança. Durante apagões prolongados, a comunicação convencional torna-se limitada, criando situações potencialmente perigosas, especialmente em ambientes com baixa ou nenhuma iluminação.


### Explicação do Projeto: Sistema de Alerta por Gestos em Apagões

#Visão Geral
Nosso projeto apresenta uma solução tecnológica para comunicação em situações de falta de energia, utilizando visão computacional e inteligência artificial para reconhecer gestos humanos como forma de pedido de ajuda. O sistema foi desenvolvido para operar mesmo em condições de baixa luminosidade, sendo especialmente útil durante emergências causadas por apagões.

#Como Funciona?

Detecção de Gestos (Python + MediaPipe): 
Utilizamos a biblioteca MediaPipe para identificar mãos e dedos em tempo real, capturando posições e movimentos específicos. O sistema reconhece três gestos de emergência principais:

- Mão aberta repetida três vezes: aciona luzes de emergência
- Polegar para cima com movimento lateral: envia alerta silencioso para equipes
- Formação de "SOS" com os dedos: dispara notificação para sistemas de monitoramento


Sistema de Alertas
Quando um gesto é identificado, o sistema:
- Ativa luzes LED (simuladas via interface)
- Exibe notificações no painel de controle

Diferenciais Tecnológicos

- Baixo custo de implementação, rodando em hardware convencional
- Solução acessível, com gestos intuitivos e interface simplificada

Aplicações Práticas
- Hospitais: comunicação silenciosa em salas cirúrgicas durante falhas de energia
- Indústrias: sistema de SOS em áreas de risco sem iluminação
- Residências: auxílio para idosos e pessoas com deficiência visual
