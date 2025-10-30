from hero import Hero_fighter, Hero_ranger
    
lucia = Hero_fighter('lucia')
luna = Hero_ranger('luna')

lucia.showInfo()        
luna.showInfo()

lucia.gainExp = 200
luna.gainExp = 250

lucia.showInfo()        
luna.showInfo()