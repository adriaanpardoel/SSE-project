start /d "%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\ IntelPowerGadget.exe

timeout 5

:: dataset: covertype, housing
:: activation: identity, logistic, tanh, relu
:: solver: lbfgs, sgd, adam
:: hidden layer size: 100 , 500, 1000
:: number of layers: 1 2 3

for %%w in (covertype, housing) do (
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

taskkill /im IntelPowerGadget.exe

pause