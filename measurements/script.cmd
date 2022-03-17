start /d "%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\ IntelPowerGadget.exe

timeout 5

:: dataset: iris, digits, wine, breast_cancer
:: activation: identity, logistic, tanh, relu
:: solver: lbfgs, sgd, adam
:: learning-rate: constant, invscaling, adaptive

for %%w in (iris, digits, wine, breast_cancer) do (
	for %%x in (identity, logistic, tanh, relu) do (
		for %%y in (lbfgs, sgd, adam) do (
			for %%z in (constant, invscaling, adaptive) do (
				"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -start
				python train_network.py --dataset %%w --hidden-layer-sizes 100 --activation %%x --solver %%y --learning-rate %%z --log-file result.csv
				"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -stop
				timeout 5
			)
		)
	)
)

taskkill /im IntelPowerGadget.exe

pause