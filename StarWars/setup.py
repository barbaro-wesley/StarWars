import cx_Freeze

executables = [cx_Freeze.Executable(
    script="game.py", icon="assets/TrupperIco.ico")]

cx_Freeze.setup(
    name="Star Wars do Marcão",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]
                           }},
    executables = executables
)


#python setup.py build   (aqui vai gerar uma pasta com o executável dentro)
#python setup.py bdist_msi (aqui vai ser um instalador de windows)


