start /d "%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\ IntelPowerGadget.exe

timeout 5

:: dataset: covertype, rcv1, iris, digit
:: activation: identity, logistic, tanh, relu
:: solver: lbfgs, sgd, adam
:: hidden layer size: 100 , 500, 1000


echo 1 Layer
for %%w in (iris, digit, rcv1, covertype) do (
	for %%x in (identity, logistic, tanh, relu) do (
		for %%y in (lbfgs, sgd, adam) do (
			for %%z in (100, 500, 1000) do (
				"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -start
				python train_network.py --dataset %%w --hidden-layer-sizes %%z --activation %%x --solver %%y  --log-file result.csv
				"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -stop
				timeout 5
			)
		)
	)
)

echo 2 Layers
for %%w in (iris, digit, rcv1, covertype) do (
	for %%x in (identity, logistic, tanh, relu) do (
		for %%y in (lbfgs, sgd, adam) do (
			for %%z in (100, 500, 1000) do (
				"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -start
				python train_network.py --dataset %%w --hidden-layer-sizes %%z %%z --activation %%x --solver %%y  --log-file result.csv
				"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -stop
				timeout 5
			)
		)
	)
)

echo 3 Layers
for %%w in (iris, digit, rcv1, covertype) do (
	for %%x in (identity, logistic, tanh, relu) do (
		for %%y in (lbfgs, sgd, adam) do (
			for %%z in (100, 500, 1000) do (
				"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -start
				python train_network.py --dataset %%w --hidden-layer-sizes %%z %%z %%z--activation %%x --solver %%y  --log-file result.csv
				"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -stop
				timeout 5
			)
		)
	)
)

taskkill /im IntelPowerGadget.exe

pause