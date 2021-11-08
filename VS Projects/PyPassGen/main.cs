namespace Namespace {
    
    using di = dict;
    
    using randint = random.randint;
    
    using System.Collections.Generic;
    
    using System;
    
    public static class Module {
        
        public static object i = 1;
        
        public static object generated_list = new List<object>();
        
        public static object second_generated_list = new List<object>();
        
        public static object length = Convert.ToInt32(input("Adja meg a jelszó hosszát: "));
        
        public static object letter_x_gen_index = randint(0, 25);
        
        public static object symbol_y_gen_index = randint(0, 24);
        
        public static object letter_z_gen_index = randint(0, 25);
        
        public static object generated_x_letter = di.lowercase_letter_list[letter_x_gen_index];
        
        public static object generated_y_symbol = di.symbol_list[symbol_y_gen_index];
        
        public static object generated_z_letter = di.uppercase_letter_list[letter_z_gen_index];
        
        static Module() {
            generated_list.extend(generated_x_letter);
            generated_list.extend(generated_y_symbol);
            generated_list.extend(generated_z_letter);
        }
        
        public static object i = 1;
    }
}
