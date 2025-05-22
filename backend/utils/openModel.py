import pickle

with open("backend/modelo_cluster_cartao_credito.pkl", "rb") as file:
    data = pickle.load(file)

print(data)