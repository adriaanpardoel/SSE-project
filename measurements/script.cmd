start /d "%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\ IntelPowerGadget.exe

timeout 5

:: activation: identity, logistic, tanh, relu
:: solver: lbfgs, sgd, adam
:: hidden layer size: 100, 300, 500
:: features: 10, 50, 100
:: samples: 10000, 20000, 50000
:: classes: 2, 3, 4

for %%u in (10, 50, 100) do (
	for %%v in (2, 3, 4) do (
		for %%w in (10000, 20000, 50000) do (
			for %%x in (identity, logistic, tanh, relu) do (
				for %%y in (lbfgs, sgd, adam) do (
					for %%z in (100, 200, 500) do (
						"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -start
						python train_network.py --features %%v --classes %%v --features %%w --hidden-layer-sizes %%z --activation %%x --solver %%y  --log-file result.csv
						"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -stop
						timeout 5
					)
				)
			)
		)
	)
)

for %%u in (10, 50, 100) do (
	for %%v in (2, 3, 4) do (
		for %%w in (10000, 20000, 50000) do (
			for %%x in (identity, logistic, tanh, relu) do (
				for %%y in (lbfgs, sgd, adam) do (
					for %%z in (100, 200, 500) do (
						"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -start
						python train_network.py --features %%v --classes %%v --features %%w --hidden-layer-sizes %%z %%z --activation %%x --solver %%y  --log-file result.csv
						"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -stop
						timeout 5
					)
				)
			)
		)
	)
)

for %%u in (10, 50, 100) do (
	for %%v in (2, 3, 4) do (
		for %%w in (10000, 20000, 50000) do (
			for %%x in (identity, logistic, tanh, relu) do (
				for %%y in (lbfgs, sgd, adam) do (
					for %%z in (100, 200, 500) do (
						"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -start
						python train_network.py --features %%v --classes %%v --features %%w --hidden-layer-sizes %%z %%z %%z --activation %%x --solver %%y  --log-file result.csv
						"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -stop
						timeout 5
					)
				)
			)
		)
	)
)

taskkill /im IntelPowerGadget.exe

pause