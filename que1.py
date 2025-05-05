def cat_hat(text):
    cat_count = text.count('cat')
    hat_count = text.count('hat')
    
    if cat_count > 0 and hat_count > 0:
        return True
    else:
        return False
result=cat_hat('catinahat')
print(result)