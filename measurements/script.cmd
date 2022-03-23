start /d "%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\ IntelPowerGadget.exe

timeout 5

:: hidden layer size: 100, 300, 500
:: features: 10, 50, 100
:: samples: 10000, 50000, 100000
:: classes: 2, 3, 7
:: layers: 1, 2, 3

for %%u in (10, 50, 100) do (
	for %%v in (2, 3, 7) do (
		for %%w in (10000, 20000, 50000) do (
			for %%z in (100, 200, 500) do (
				"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -start
				python train_network.py --features %%v --classes %%v --features %%w --hidden-layer-sizes %%z --log-file result.csv
				"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -stop
				timeout 5
			)
		)
	)
)

for %%u in (10, 50, 100) do (
	for %%v in (2, 3, 7) do (
		for %%w in (10000, 20000, 50000) do (
			for %%z in (100, 200, 500) do (
				"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -start
				python train_network.py --features %%v --classes %%v --features %%w --hidden-layer-sizes %%z %%z --log-file result.csv
				"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -stop
				timeout 5
			)
		)
	)
)

for %%u in (10, 50, 100) do (
	for %%v in (2, 3, 7) do (
		for %%w in (10000, 20000, 50000) do (
			for %%z in (100, 200, 500) do (
				"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -start
				python train_network.py --features %%v --classes %%v --features %%w --hidden-layer-sizes %%z %%z %%z --log-file result.csv
				"%PROGRAMFILES%"\Intel\"Power Gadget 3.6"\IntelPowerGadget.exe -stop
				timeout 5
			)
		)
	)
)


taskkill /im IntelPowerGadget.exe

pause