%title: Intro rapide à la cryptographie asymétrique
%author: Uriel Corfa
%date: 2020-09-08


Bonjour, parlons un peu de crypto.


Avec pas trop de maths, svp.

------------------------------------

-> # Disclaimer <-
========================

Cette présentation ne reflète que mon point de vue et mes opinions, et
pas ceux de mon employeur.

------------------------------------

-> # L'histoire de la cryptographie (abrégée) <-
========================

vers -1600: tablettes en argile chiffrées par *substitution*

vers -800: _Al-Kindi_ invente la *cryptanalyse*

1939-45: La cryptographie devient essentielle, _Alan Turing_ & les
équipes de Bletchley Park décodent le chiffrement de la machine Enigma

1945: _Claude Shannon_ définit la *sécurité inconditionnelle*

1976: _Whitfeld Diffie_ & _Martin Hellman_ inventent le *chiffrement asymétrique*

------------------------------------

-> # Chiffrement par substitution <-
========================

-> A B C D E ... X Y Z <-
-> ↓ ↓ ↓ ↓ ↓     ↓ ↓ ↓ <-
-> B C D E F ... Y Z A <-

------------------------------------

-> # Chiffrement par substitution <-
========================

-> A B C D E ... X Y Z <-
-> ↓ ↓ ↓ ↓ ↓     ↓ ↓ ↓ <-
-> B C D E F ... Y Z A <-

-> SYMMETRIC CRYPTOGRAPHY <-
-> TZNNFUSJD DSZQUPHSBQIZ <-

------------------------------------

-> # XOR cipher <-
========================

-> XOR | 0 | 1 <-
->   0 | 0 | 1 <-
->   1 | 1 | 0 <-

n XOR x XOR x == n

------------------------------------

-> # XOR cipher <-
========================

H   72  1001000
e  101  1100101
y  121  1111001
\!   21  0010101

"Hey!" -> 1001000 1100101 1111001 0010101

------------------------------------

-> # XOR cipher <-
========================

H   72  1001000
e  101  1100101
y  121  1111001
\!   21  0010101

"Hey!" -> 1001000 1100101 1111001 0010101
"kR0g" -> 1101011 1010010 0110000 1010010

------------------------------------

-> # XOR cipher <-
========================

H   72  1001000
e  101  1100101
y  121  1111001
\!   21  0010101

"Hey!" -> 1001000 1100101 1111001 0010101
"kR0g" -> _1101011 1010010 0110000 1010010_
a XOR b   0100011 0110111 1001001 1000111 -> "#7sq"

------------------------------------

-> # XOR cipher <-
========================

H   72  1001000
e  101  1100101
y  121  1111001
\!   21  0010101

"Hey!" -> 1001000 1100101 1111001 0010101
"kR0g" -> _1101011 1010010 0110000 1010010_
a XOR b   0100011 0110111 1001001 1000111 -> "#7sq"

"#7sq" -> 0100011 0110111 1001001 1000111
"kR0g" -> _1101011 1010010 0110000 1010010_
a XOR b   1001000 1100101 1111001 0010101 -> "Hey!"

------------------------------------

-> # XOR cipher <-
========================

Si len(key) >= len(message), on obtient la *sécurité inconditionnelle*.

Bien si:
* On sait d'avance à qui on veut parler;
* On peut échanger une clef suffisament longue préalablement.

------------------------------------

-> # Chiffrement symétrique <-
========================

Le chiffrement par substitution et le chiffrement XOR sont deux
algorithmes dits *symétriques*: l'expéditeur et le destinataire
connaissent tous les deux un *secret partagé*.

D'autres algorithmes symétriques: AES, Blowfish, Twofish, ...

------------------------------------

-> # Chiffrement asymétrique <-
========================

Mais si on ne peut pas partager un secret préalablement ?

-> Chiffrement asymétrique <-

L'expéditeur et le destinataire ont des *clés différentes*.

------------------------------------

-> # Algorithme RSA <-
========================

Inventé en 1977 par _Ron Rivest_, _Adi Shamir_ et _Leonard Adleman_.

Alice veut écrire à Bob, mais ils ne partagent pas de secret.

Bob génère une *clé publique* et une *clé privée* puis donne la clé
publique à Alice. Alice chiffre son message en utilisant la clé
publique de Bob. Seule la clé privée peut déchiffrer ce message, et
seul Bob a une copie de la clé privée.

------------------------------------

-> # Mais comment c'est possible ? <-
========================

MATH TIME

(juste un peu)

------------------------------------

-> # Génération de clé RSA <-
========================

1. Bob choisit 2 nombres premiers, p et q.
   Bob calcule n = p \* q.

Disons p = 61, q = 53, n = 3233.

------------------------------------

-> # Génération de clé RSA <-
========================

1. Bob choisit 2 nombres premiers, p = 61 et q = 53.
   Bob calcule n = p \* q = 3233.

2. Bob calcule φ(n) = (p - 1) \* (q - 1) = 3120.

------------------------------------

-> # Génération de clé RSA <-
========================

1. Bob choisit 2 nombres premiers, p = 61 et q = 53.
   Bob calcule n = p \* q = 3233.

2. Bob calcule φ(n) = (p - 1) \* (q - 1) = 3120.

3. Bob choisit un entier e tel que 1 < e < φ, et e et φ sont premiers entre eux.
   Disons e = 17.
   Bob envoie e et n à Alice, en public. C'est la clé publique.

------------------------------------

-> # Génération de clé RSA <-
========================

1. Bob choisit 2 nombres premiers, p = 61 et q = 53.
   Bob calcule n = p \* q = 3233.

2. Bob calcule φ(n) = (p - 1) \* (q - 1) = 3120.

3. Bob choisit un entier e = 17 tel que 1 < e < φ, et e et φ sont premiers entre eux.

4. Bob calcule d = (1 + x*φ)/e pour un x tel que d soit un nombre entier.
   d = 2753.
   Bob conserve d secrètement. d et n sont la clé privée.

------------------------------------

-> # Chiffrement RSA <-
========================

Alice a reçu de Bob: n = 3233 et e = 2753.
Elle veut lui envoyer un nombre secret, m = 123.

Alice calcule c = mᵉ % n = 855 et envoie le résultat à Bob.

------------------------------------

-> # Déchiffrement RSA <-
========================

Alice a reçu de Bob: n = 3233 et e = 2753.
Elle veut lui envoyer un nombre secret, m = 123.

Alice calcule c = mᵉ % n = 855 et envoie le résultat à Bob.

Bob reçoit c = 855 connait d = 2573 and n = 3233.

Bob calcule m = cᵈ % n = 123 et retrouve le secret d'Alice.

------------------------------------

-> # Ce que ça veut dire <-
========================

Je peux vous donner ma *clé publique* en public.

Vous pouvez vous en servir pour m'envoyer un message que seule ma
*clé privée* peut déchiffrer.

On peut se parler complètement en public sans qu'on nous comprenne et
sans se mettre d'accord préalablement sur un secret partagé.

------------------------------------

-> # Ce que ça veut dire <-
========================

Mais n'importe qui peut vous donner une clé publique et prétendre être
moi.

Et n'importe qui peut utiliser ma clé publique pour m'envoyer un
message en prétendant être vous.

On a donc la *confidentialité*, mais il nous manque la notion d' *attribution*.

------------------------------------

-> # Signature <-
========================

Heureusement, on peut utiliser un algorithme de chiffrement
asymétrique à l'envers comme outil de signature.

1. Je génère une deuxième paire de clés publique/privée.
2. Je partage ma clé _privée_ mais je garde secrète la clé _publique_.
3. Je suis le seul à pouvoir chiffrer des messages avec cette clé,
   mais n'importe qui peut les déchiffrer !
4. Donc si vous pouvez déchiffrer un message avec cette clé, vous
   savez qu'il est de moi.

On parle plutôt de "clé de signature" et de "clé de vérification" ou
d'"authentification".

------------------------------------

-> # Signature <-
========================

Heureusement, on peut utiliser un algorithme de chiffrement
asymétrique à l'envers comme outil de signature.

1. Je génère une deuxième paire de clés publique/privée.
2. Je partage ma clé _privée_ mais je garde secrète la clé _publique_.
3. Je suis le seul à pouvoir chiffrer des messages avec cette clé,
   mais n'importe qui peut les déchiffrer !
4. Donc si vous pouvez déchiffrer un message avec cette clé, vous
   savez qu'il est de moi.

On parle plutôt de "clé de signature" et de "clé de vérification" ou
d'"authentification".

Avec RSA, même pas besoin de générer une nouvelle clé, on peut
utiliser *d* pour signer et *e* pour vérifier la signature.

------------------------------------

-> # Certificats <-
========================

Maintenant, avec votre clé publique, je peux:

* *Chiffrer* des messages qui vous sont destinés;
* *Authentifier* des messages que vous avez envoyé.

Mais comment m'assurer que cette clé publique est bien à vous ?

On peut se rencontrer en personne et échanger des clés.

Pas pratique pour parler à des inconnus.

------------------------------------

-> # Autorités de certification <-
========================

On peut faire appel à une *Autorité de Certification* (CA).

* Je leur envoie ma clé publique;
* Ils vérifient mon identité;
* Ils *signent* un document qui dit:

> La clé publique 1234abcd... appartient à Uriel Corfa
> Signé par: SomeCertificateAuthority.com

On appelle ce document un certificat.

------------------------------------

-> # Certificats <-
========================

Demo time!

------------------------------------

-> # Aller plus loin <-
========================

* GPG: génerez votre propre paire de clés, envoyez des emails avec, signez vos commits Git ou les binaires que vous publiez, et bien plus:
   * https://gnupg.org/
* Installez un serveur web, obtenez un certificat gratuitement:
   * https://letsencrypt.org/getting-started
* Installez un serveur de messagerie Matrix et apprenez à gérer des
  clés pour chacun:
   * https://matrix.org
* Lisez les livres de Bruce Schneier
   * https://www.schneier.com/
   * _Cryptography Engineering_

------------------------------------

-> # Mais attention <-
========================

N'utilisez pas votre propre algorithme de cryptographie !

Utilisez une lib. Ecoutez les cryptographes professionels. Ne faites
pas confiance à n'importe qui sur StackOverflow. Lisez Bruce Schneier.

-----------------------------------

-> # Questions ? <-
========================

-----------------------------------

-> # The Diffie-Hellman key exchange <-
========================

Alice and Bob wants to establish a shared secret.

1. Pick 2 numbers publicly, p and g.
   p is a prime, let's say 23.
   g is a primitive root modulo p, let's say 5.

------------------------------------

-> # The Diffie-Hellman key exchange <-
========================

Alice and Bob wants to establish a shared secret.

1. Pick 2 numbers publicly, p and g.
   p is a prime, let's say 23.
   g is a primitive root modulo p, let's say 5.

p and g can be picked long in advance for everyone publicly.

For example, these real constants for 2048bit DSA keys:

    p = fca682ce 8e12caba 26efccf7 110e526d b078b05e decbcd1e b4a208f3
        ae1617ae 01f35b91 a47e6df6 3413c5e1 2ed0899b cd132acd 50d99151
        bdc43ee7 37592e17
    g = 678471b2 7a9cf44e e91a49c5 147db1a9 aaf244f0 5a434d64 86931d2d
        14271b9e 35030b71 fd73da17 9069b32e 2935630e 1c206235 4d0da20a
        6c416e50 be794ca4

------------------------------------

-> # The Diffie-Hellman key exchange <-
========================

Alice and Bob wants to establish a shared secret.

1. Pick 2 numbers publicly, p = 23 and g = 5.

2. Alice choses a secret integer a, let's say 4.
   Alice sends Bob Pa = gᵃ % p = 5⁴ % 23 = 4

3. Bob choses a secret integer b, let's say 3.
   Bob sends Alice Pb = gᵇ % p = 5³ % 23 = 10.

------------------------------------

-> # The Diffie-Hellman key exchange <-
========================

Alice and Bob wants to establish a shared secret.

1. Pick 2 numbers publicly, p = 23 and g = 5.

2. Alice choses a secret integer a, let's say 4.
   Alice sends Bob Pa = gᵃ % p = 5⁴ % 23 = 4

3. Bob choses a secret integer b, let's say 3.
   Bob sends Alice Pb = gᵇ % p = 5³ % 23 = 10.
  
4. Alice computes s = Pbᵃ % p = 10⁴ % 23 = 18

5. Bob computes s = Paᵇ % p = 4³ % 23 = 18

------------------------------------

-> # The Diffie-Hellman key exchange <-
========================

Alice and Bob wants to establish a shared secret.

1. Pick 2 numbers publicly, p = 23 and g = 5.

2. Alice choses a secret integer a, let's say 4.
   Alice sends Bob Pa = gᵃ % p = 5⁴ % 23 = 4

3. Bob choses a secret integer b, let's say 3.
   Bob sends Alice Pb = gᵇ % p = 5³ % 23 = 10.
  
4. Alice computes s = Pbᵃ % p = 10⁴ % 23 = 18

5. Bob computes s = Paᵇ % p = 4³ % 23 = 18

Alice and Bob share a secret, S=18.

Someone who listens has Pa and Pb but not a and b, which Alice and Bob
kept secret, and can't derive S.

