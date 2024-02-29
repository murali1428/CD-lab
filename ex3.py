e=u'\u03b5'
p=[]

class Prod:
  def __init__(self, name, products):
    self.name=name
    self.products=products
  
  def print(self):
    s = f'{self.name} -> '
    for p in self.products:
      s+= f' {p} |'
    s=s.rstrip('|')
    print(s)
    
def trans():
  for x in p:
    alpha=[];beta=[]
    for product in x.products:
      if x.name==product[0]:
        alpha.append(product[1:])
      else:
        beta.append(product)
        
    if alpha:
      for i in range(len(beta)):
        beta[i]=f"{beta[i]}{x.name}'"
      for i in range(len(alpha)):
        alpha[i]=f"{alpha[i]}{x.name}'"
      alpha.append(e)
      x.products =beta
      p.append(Prod(f"{x.name}'",alpha))
        
    
n = int(input("No of production: "))
for i in range(n):
  ip = input(f"Production {i+1}: ")
  name, prods = ip.split(' -> ')
  products = prods.split(' | ')
  p.append(Prod(name, products))
  
print('Productions:')
for x in p: x.print()
print('Transforming...')
trans()
for x in p: x.print()
