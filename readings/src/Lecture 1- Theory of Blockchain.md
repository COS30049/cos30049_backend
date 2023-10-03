---
title: Theory of Blockchain
tags:
  - COS30049/lectures
---
## History and Motivations

>[!resource]- Read
>
>[[../../resources/Session 1 - 1 - History and Motivation.pdf|Session 1 - 1 - History and Motivation]]

>[!media]- Watch
>
>![[../../resources/Sess1-1 History and Motivations.mp4|Sess1-1 History and Motivations]]
>

- Digital coins emerged before the creation Bitcoin but do not gain popularity. 
- Bitcoin first introduced in 2008 with domain [bitcoin.org](https://bitcoin.org) registered and later that year made its ***white paper***[^1] published and created open source project on [SourceForge.Net](https://sourceforge.net).
- In Jan 3 2009, first block 'Genesis block' created and 'Bitcoin' was released and announced in three months later. The first transaction was done in the end of the same year.

Bitcoin has received dividing opinions at first by the public and was against by the government. However, nowadays as we know, it is well-established, and has high capital market. Bitcoin has gain its fame as it was used as payment in a black market called Silk Road for anonymity.

[^1]: article published without peer-review process

## Basic Security Services and Definitions

>[!resource]- Read
>
>![[../../resources/Session 1 - 2 - Basic Security Services and Definitions.pdf|Session 1 - 2 - Basic Security Services and Definitions]]

>[!media]- Watch
>
>![[../../resources/Sess1-2 Basic Security Services and Definitions.mp4]]

### Fundamental Security Services

1. **Confidentiality**
   Keeping the information hidden from the eyes of other - encryption
   
2. **Integrity**
   Making sure data is not modified or tampered with
   
3. **Availability**
   Service should be up and available. Availability rate is often represented with `uptime`
   Attack to lower this rate is DDoS(Distributed Denial of Service attacks)
   - **SYN Flooding**: SYN packets are flooding the server, without responding to the target server with ACK packet after receiving the SYN/ACK packets from the target server to finish the handshake process. This causes the server to keep waiting until is is exhausted.
   - **Reflection DoS Attack**: Slave servers/hosts are instructed to send a request to the victim server and put the victim IP address as the Source in the packet. The requests are then received by the victim server and then floods the network with the reply, which exhausts the bandwidth. 
---
4. **Authentication**
   Making sure that the message is actually coming from the person claimed in the message.

5. **Authorization**
   Giving permission to access resources. This is related to access-control topic.
   
6. **Non-repudiation**
   Making sure no one can deny what he/she has done.

## Terminology of the Security Domain

>[!resource]- Read
>
>![[../../resources/Session 1 - 3 - Terminology of the Security Domain.pdf|Session 1 - 3 - Terminology of the Security Domain]]

>[!media]- Watch
>
>![[../../resources/Sess1-3 Terminology of the Security Domain.mp4|Sess1-3 Terminology of the Security Domain]]