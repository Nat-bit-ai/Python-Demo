def lower_to_upper(statement):
    if (statement == statement.upper()):
        return statement
    else:
        return statement.upper()

prompt = input("Enter ur name:")
print(lower_to_upper(prompt))