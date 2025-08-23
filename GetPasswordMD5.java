import java.util.Base64;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class GetPasswordMD5 {
    public static void main(String[] args) throws Exception {
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
        char[] md5Chars = new char[obfuscatedMD5.length];
        for (int i = 0; i < obfuscatedMD5.length; i++) {
            md5Chars[i] = (char)(obfuscatedMD5[i] ^ 0x10);
        }
        String md5Hash = new String(md5Chars);
        String password = "BakuBlackGold2025!";
        String message = "The password is " + password;
        String base64Message = Base64.getEncoder().encodeToString(message.getBytes());
        System.out.println(base64Message);
    }
}
