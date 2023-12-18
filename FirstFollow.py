class First_Follow():
    def __init__(self, grammar:dict):
        self.grammar = grammar
        self.non_terminals = grammar.keys()
        self.ruls = [item for sublist in grammar.values() for item in sublist]
        
        
    def compute_first(self, variable):
        
        first = set()
        
        productions = self.grammar[variable]
        for production in productions:
            if production[0].islower():
                first.add(production[0])
            else:
                first |= self.compute_first(production[0])
                
        return first
                    
    def compute_follow(self, variable):
        follow = set()
                        
        return follow
            
        

    def print_sets(self):
        print("First Sets:")
        for non_terminal in self.non_terminals:
            print(f"{non_terminal}: {self.compute_first(non_terminal)}")

        # print("\nFollow Sets:")
        # for non_terminal in self.non_terminals:
        #     print(f"{non_terminal}: {self.compute_follow(non_terminal)}")
    
    
def main():
    example_grammar = {
    'S': ['Aa', 'Bb'],
    'A': ['ε', 'Ba'],
    'B': ['b', 'ε']
    }
    
    ff = First_Follow(example_grammar)
    
    ff.print_sets()
    

if __name__ == '__main__':
    main()