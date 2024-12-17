class Getime:
     def __init__(self, total_day=8070):
          self.tdays = total_day
          self.thours = self.tdays * 24
          self.tinvested = []
     
     def insertime(self,**args):
          """Getime\
          >>> GET TIME IN HOURS PER DAY     
          """
          check = 0
          for i in args.values():
               check = check + i
          if(check!=24):
               print("NOT GIVEN 24 HOURS")
          else:
               for key, value in args.items():
                    self.tinvested.append({key:value})

     def invested_time(self):
          a = self.tinvested
          print('_'*20)
          for i in range(len(a)):
               for key,value in a[i].items():
                    print('|',key,' | ',value)
                    print('|','-'*len(key),' |','-'*5)
          print('|','_'*18)

     def time_invested(self, thabit:dict):
          key = list(thabit.keys())[0]
          value = list(thabit.values())[0]
          total_hours_spent = value * self.tdays
          p_age = total_hours_spent/self.thours * 100
          result = {
                         key:f"{total_hours_spent} hrs",
                         'over':f"{self.thours} hrs",
                         'p_age':f"{p_age} %"
                    }
          return result

     def total_investment(self):
          report = []
          for i in self.tinvested:
               r = self.time_invested(i)
               report.append(r)
          for i in report:
               print(i)

if __name__=='__main__':
     dcim = Getime()
     dcim.insertime(
          sleep=9,
          study=2,
          eating=3,
          misspend=5,
          motivated=5
     )
     dcim.total_investment()
