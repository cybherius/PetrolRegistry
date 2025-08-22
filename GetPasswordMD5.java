import java.util.Base64;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class GetPasswordMD5 {
    public static void main(String[] args) throws Exception {
        // Step 1: Obfuscated MD5 hash of the password
        // Original password: BakuBlackGold2025!
        // MD5 hash: 8c9c7a7df9c6f1f9c5b4b7b2b1f1d0c8
        // Obfuscation: XOR each char with 0x10
        char[] obfuscatedMD5 = {
            '8'^0x10,'c'^0x10,'9'^0x10,'c'^0x10,
            '7'^0x10,'a'^0x10,'7'^0x10,'d'^0x10,
            'f'^0x10,'9'^0x10,'c'^0x10,'6'^0x10,
            'f'^0x10,'1'^0x10,'f'^0x10,'9'^0x10,
            'c'^0x10,'5'^0x10,'b'^0x10,'4'^0x10,
            'b'^0x10,'7'^0x10,'b'^0x10,'2'^0x10,
            'b'^0x10,'1'^0x10,'f'^0x10,'1'^0x10,
            'd'^0x10,'0'^0x10,'c'^0x10,'8'^0x10
        };

        // Step 2: Deobfuscate MD5 hash
        char[] md5Chars = new char[obfuscatedMD5.length];
        for (int i = 0; i < obfuscatedMD5.length; i++) {
            md5Chars[i] = (char)(obfuscatedMD5[i] ^ 0x10);
        }
        String md5Hash = new String(md5Chars);

        // Just to show the MD5 hash (optional)
        System.out.println("Deobfuscated MD5: " + md5Hash);

        // Step 3: "Reverse" hash (simulate retrieval of password)
        // In real scenario, player uses hints / hash cracking
        String password = "BakuBlackGold2025!";

        // Step 4: Build final message
        String message = "The password is " + password;

        // Step 5: Encode message in Base64
        String base64Message = Base64.getEncoder().encodeToString(message.getBytes());

        // Step 6: Print Base64 message
        System.out.println(base64Message);
    }
}
