let publicKey = {};
let privateKey = {};

function generateKeys() {
  // Generate two large prime numbers
  let p = generateLargePrime();
  let q = generateLargePrime();

  // Calculate n = p * q
  let n = p * q;

  // Calculate the totient function φ(n) = (p-1)(q-1)
  let phi = (p - 1) * (q - 1);

  // Choose an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
  let e = 65537; // Common choice for e

  // Calculate d such that d ≡ e^(-1) (mod φ(n))
  let d = modInverse(e, phi);

  publicKey = { e, n };
  privateKey = { d, n };

  document.getElementById("publicKey").innerText = `(${e}, ${n})`;
  document.getElementById("privateKey").innerText = `(${d}, ${n})`;
}

function encrypt() {
  let text = document.getElementById("plainText").value;
  let encryptedText = text
    .split("")
    .map((char) => {
      let m = char.charCodeAt(0);
      let c = modExp(m, publicKey.e, publicKey.n);
      return c;
    })
    .join(" ");

  document.getElementById("encryptedText").innerText = encryptedText;
}

function decrypt() {
  let cipherText = document.getElementById("cipherText").value;
  let decryptedText = cipherText
    .split(" ")
    .map((num) => {
      let c = parseInt(num);
      let m = modExp(c, privateKey.d, privateKey.n);
      return String.fromCharCode(m);
    })
    .join("");

  document.getElementById("decryptedText").innerText = decryptedText;
}

function generateLargePrime() {
  // For simplicity, returning small primes for demonstration. Replace with a proper large prime generator for real applications.
  const primes = [
    61, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2,
  ];
  return primes[Math.floor(Math.random() * primes.length)];
}

function gcd(a, b) {
  while (b !== 0) {
    let t = b;
    b = a % b;
    a = t;
  }
  return a;
}

function modInverse(e, phi) {
  let [g, x] = extendedGCD(e, phi);
  if (g !== 1) {
    throw new Error("No modular inverse exists");
  }
  return ((x % phi) + phi) % phi;
}

function extendedGCD(a, b) {
  if (b === 0) {
    return [a, 1, 0];
  }
  let [g, x1, y1] = extendedGCD(b, a % b);
  return [g, y1, x1 - Math.floor(a / b) * y1];
}

function modExp(base, exp, mod) {
  if (exp === 0) return 1;
  let half = modExp(base, Math.floor(exp / 2), mod);
  let result = (half * half) % mod;
  if (exp % 2 !== 0) {
    result = (result * base) % mod;
  }
  return result;
}
