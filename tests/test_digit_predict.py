import sys
import os
sys.path.append(os.path.abspath('.')) 

import torch
from torchvision import datasets, transforms
from src.vision.mnist_classifier import DigitClassifier

def predict_digit():
    model = DigitClassifier()
    model.load_state_dict(torch.load("models/mnist_model.pth"))
    model.eval()

    transform = transforms.ToTensor()
    test_data = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    image, label = test_data[0]

    with torch.no_grad():
        output = model(image.unsqueeze(0))
        predicted = output.argmax(dim=1).item()

    print(f"Actual: {label} | Predicted: {predicted}")

predict_digit()
