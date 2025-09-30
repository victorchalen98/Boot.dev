def purchase_item(price, gold_available):
        actual_money = gold_available - price
        if gold_available < price:
            raise Exception("not enough gold")
        else:
              return actual_money
            
