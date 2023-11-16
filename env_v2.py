# The EnvironmentManager class keeps a mapping between each variable name (aka symbol)
# in a brewin program and the Value object, which stores a type, and a value.
class EnvironmentManager:
    
    
    def all_vars(self):
        all_variables = set()
        for env in self.environment:
            all_variables.update(env.keys())
        return all_variables
    
    def __init__(self):
        self.environment = [{}]

    # returns a VariableDef object
    def get(self, symbol):
        for env in reversed(self.environment):
            if symbol in env:
                return env[symbol]

        return None

    def set(self, symbol, value):
        for env in reversed(self.environment):
            if symbol in env:
                env[symbol] = value
                return

        # symbol not found anywhere in the environment
        self.environment[-1][symbol] = value

    # create a new symbol in the top-most environment, regardless of whether that symbol exists
    # in a lower environment
    def create(self, symbol, value):
        self.environment[-1][symbol] = value

    # used when we enter a nested block to create a new environment for that block
    def push(self):
        self.environment.append({})  # [{}] -> [{}, {}]

    # used when we exit a nested block to discard the environment for that block
    def pop(self):
        self.environment.pop()
        
        
    def contains(self, symbol):
        return symbol in self.environment[-1]   

    def __repr__(self):
        current_env = self.environment[-1]
        result = "---- Current Environment ----\n"
        for symbol, value in current_env.items():
            result += f"{symbol}: {value}\n"
        result += "\n---------------------------\n"
        return result
    
    
    
    def printall(self):
        result = ""
        for index, env in enumerate(self.environment):
            result += "---- New Environment ----\n"
            result += f"Environment {index}:\n"
            for symbol, value in env.items():
                result += f"  {symbol}: {value}\n"
        return result