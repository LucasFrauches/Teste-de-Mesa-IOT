def main():
#processamento
  
  with open("dadosEntrada.txt", "r") as a:
    idade = [int(x) for x in a.readlines()]
  
  n = len(idade)
  
  for i in range(n):
    for j in range(0, n-i-1):

      if idade[j] > idade[j+1] :
        
        idade[j], idade[j+1] = idade[j+1], idade[j]
  
#saída      
  print(f'{idade}')

if __name__ == ("__main__"):
  main()
