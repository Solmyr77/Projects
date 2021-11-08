namespace dict {
    
    using @string;
    
    using System.Linq;
    
    using System.Collections.Generic;
    
    public static class Module {
        
        public static object lowercase_letter_list = @string.ascii_lowercase.ToList();
        
        public static object symbol_list = new List<object> {
            "|",
            "Ä",
            "€",
            "÷",
            "×",
            "ä",
            "đ",
            "[",
            "]",
            "ł",
            "Ł",
            "$",
            "ß",
            "¤",
            "<",
            ">",
            "#",
            "&",
            "@",
            "{",
            "}*",
            "/",
            "+",
            "-",
            ".",
            ","
        };
        
        public static object uppercase_letter_list = @string.ascii_uppercase.ToList();
    }
}
