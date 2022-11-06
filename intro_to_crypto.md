%title: A quick intro to asymmetric cryptography
%author: Uriel Corfa
%date: 2022-10-26

Hi, let's talk about cryptography.

We won't be using much math today.

------------------------------------

-> # Disclaimer <-
========================

The views and opinions expressed in this presentation are my own, not
those of my employer.

------------------------------------

-> # What this talk is about <-
========================

Cryptography is everywhere.

We all have an intuition about it.

------------------------------------

-> # What this talk is about <-
========================

Cryptography is everywhere

We all have an intuition about it

How can we talk to a website we've never met, securely?

Math is **weird** and we can use that to our advantage

------------------------------------

-> # A brief history of cryptography <-
========================

~1600 BC: clay tablets using a *substitution cipher*

~800 AD: _Al-Kindi_ invents *cryptanalysis*

WW2: Cryptography gets serious, _Alan Turing_ & Bletchley Park
scientists break Germany's Enigma machine

1945: _Claude Shannon_ defines *perfect secrecy*

1976: _Whitfeld Diffie_ & _Martin Hellman_ invent *asymmetric cryptography*

------------------------------------

-> # Substitution cipher <-
========================

-> A B C D E ... X Y Z <-
-> ↓ ↓ ↓ ↓ ↓     ↓ ↓ ↓ <-
-> B C D E F ... Y Z A <-

------------------------------------

-> # Substitution cipher <-
========================

-> A B C D E ... X Y Z <-
-> ↓ ↓ ↓ ↓ ↓     ↓ ↓ ↓ <-
-> B C D E F ... Y Z A <-

-> SUBSTITUTION CIPHER <-
-> TVCTUJUVUJPO DJQIFS <-

------------------------------------

-> # Substitution cipher <-
========================

-> A B C D E ... X Y Z <-
-> ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ <-
-> B C D E F ... Y Z A <-

-> SUBSTITUTION CIPHER <-
-> TVCTUJUVUJPO DJQIFS <-

-> TVCTUJUVUJPO DJQIFS <-
-> SUBSTITUTION CIPHER <-

------------------------------------

-> # Substitution cipher <-
========================

Easy to understand, easy to use.

Easy to break.

------------------------------------

-> # XOR cipher <-
========================

-> XOR | 0 | 1 <-
->   0 | 0 | 1 <-
->   1 | 1 | 0 <-

(n XOR x) XOR x == n

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

If len(key) >= len(message), this provides *perfect secrecy*.

Great if:
* You know who you'll talk to in advance;
* You can give them enough key material in a trusted way.

------------------------------------

-> # Symmetric cryptography <-
========================

Both these ciphers are example of symmetric encryption algorithms: the
sender and the receiver hold a *shared secret*.

More complex examples of heavily used symmetric ciphers: AES,
Blowfish, Twofish, ...

------------------------------------

-> # Asymmetric cryptography <-
========================

What if you can't establish a shared secret in advance?

Enter asymmetric cryptography.

The sender and the receiver have *different keys*.

------------------------------------

-> # The RSA algorithm <-
========================

Invented in 1977 by _Ron Rivest_, _Adi Shamir_ and _Leonard Adleman_.

Alice wants to send a message to Bob, but they didn't establish a
shared secret.

Bob generates a *public key* and a *private key* and gives Alice the
public key. Alice encrypts her message using Bob's public key, but
only the private key can decrypt it, and only Bob has the private key.

------------------------------------

-> # How's that even possible? <-
========================

This is the math portion of the talk.

------------------------------------

-> # RSA key generation <-
========================

1. Bob picks two random prime numbers, p and q.
   Bob calculates n = p \* q.

Let's say p = 61, q = 53, n = 3233.

------------------------------------

-> # RSA key generation <-
========================

1. Bob picks two random prime numbers, p = 61 and q = 53.
   Bob calculates n = p \* q = 3233.

2. Bob calculates φ(n) = (p - 1) \* (q - 1) = 3120.

------------------------------------

-> # RSA key generation <-
========================

1. Bob picks two random prime numbers, p = 61 and q = 53.
   Bob calculates n = p \* q = 3233.

2. Bob calculates φ = (p - 1) \* (q - 1) = 3120.

3. Bob choses an integer e such that 1 < e < φ, and e and φ are coprime.
   Let's say e = 17.
   Bob shares e and n publicly to Alice.

------------------------------------

-> # RSA key generation <-
========================

1. Bob picks two random prime numbers, p = 61 and q = 53.
   Bob calculates n = p \* q = 3233.

2. Bob calculates φ = (p - 1) \* (q - 1) = 3120.

3. Bob choses an integer e = 17 such that 1 < e < φ, and e and φ are coprime.

4. Bob computes d = (1 + x*φ)/e picking x so that d is an integer.
   d = 2753.
   Bob keeps d private.

------------------------------------

-> # RSA encryption <-
========================

Alice has Bob's n = 3233 and e = 2753.
She wants to send a secret number m = 123.
   
Alice computes c = mᵉ % n = 855 and sends that to Bob.

------------------------------------

-> # RSA decryption <-
========================

Alice has Bob's n = 3233 and e = 2753.
She wants to send a secret number m = 123.
   
Alice computes c = mᵉ % n = 855 and sends that to Bob.

Bob receives c = 855 and knows d = 2573 and n = 3233.

Bob computes m = cᵈ % n = 123.

------------------------------------

-> # What this means <-
========================

I can give you my *public key* in a public forum.

You can use this to encrypt a message so that only my *private key*
can decrypt it.

We can communicate in the open without needing to exchange keys
beforehand.

------------------------------------

-> # What this means <-
========================

But of course, anyone can give you a public key and pretend to be me.

And anyone can use my public key and send me messages and pretend to
be you.

We have *confidentiality* but we need *authentication*.

------------------------------------

-> # Signing <-
========================

Fortunately, we can use any asymmetric algorithm for signing.

1. I generate a second public/private key pair.
2. I share the _private_ part, keep the _public_ part.
3. Only I can encrypt messages with this key, but anyone can decrypt them!
4. So if you can decrypt a message using this key, you know it's from me.

In this scenario, we say we have a *signing* key and a *verification* key.

------------------------------------

-> # Signing <-
========================

Fortunately, we can use an asymmetric algorithm for signing.

1. Generate a second public/private key pair.
2. Share the _private_ part, keep the _public_ part.
3. Only I can encrypt messages with this key, but anyone can decrypt them!
4. So if you can decrypt a message using this key, you know it's from me.

In this scenario, we say we have a *signing* key and a *verification* key.

With RSA, you don't actually need to generate a new key, you can use
*d* to sign and *e* to verify.

------------------------------------

-> # Certificates <-
========================

Now, if I have your public key, I can:

* *Encrypt* messages to you
* *Authenticate* messages from you

How do I know I have your public key, and not someone else's?

We could meet in person to echange keys.

Not practical if you want to talk to a stranger.

------------------------------------

-> # Certificate Authorities <-
========================

Introducing: *Certificate Authorities* (CA).

* I send them my public key
* They verify that I am in fact who I claim to be
* They *sign* a document that says:

> Public key 1234abcd... belongs to Uriel Corfa
> Signed by: SomeCertificateAuthority.com

That document is called a certificate.

------------------------------------

-> # Certificates <-
========================

Demo time!

------------------------------------

-> # Why most crypto is still symmetric <-
========================

Asymmetric cryptography is very cool.

It's also very expensive to use.

We can use *asymmetric crypto* to negotiate a *shared secret*.

-----------------------------------

-> # The Diffie-Hellman key exchange <-
========================

Asymmetric cryptography is expensive

We can use *asymmetric crypto* to negotiate a *shared secret*

We could simply use RSA to establish a channel, generate a secret key,
share it over that channel, and switch to AES

But we don't need to!

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

------------------------------------

-> # Go further <-
========================

* GPG: generate your own personal keypair, use it for email, to sign
  Git commits or binaries you release
   * https://gnupg.org/
* Install a webserver, and get it a public certificate
   * https://letsencrypt.org/getting-started
* Install a decentralized Matrix instant messaging server and enjoy
  managing keys
   * https://matrix.org
* Read Bruce Schneier
   * https://www.schneier.com/
   * _Cryptography Engineering_

------------------------------------

-> # A word of warning <-
========================

Do not roll your own crypto!

Use abstractions. Trust cryptographers. Don't trust random people on
the Internet. Read Bruce Schneier.

-----------------------------------

-> # Questions ? <-
========================
