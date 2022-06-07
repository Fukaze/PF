import sys
sys.path.append("C:\Program Files\DIgSILENT\PowerFactory 2020 SP2A\Python\\3.8") #OJO CON NUMEROS COMO NOMBRE DE CARPETA
print(sys.path)
import powerfactory as pf


#sys.path.append("C:\Program Files\DIgSILENT\PowerFactory 2020 SP2A")


try:
    App = pf.GetApplication() #[str username = None,][str password = None,][str commandLineArguments = None]
    App.EchoOn()

    print("Oru Raito")

    #project = App.CreateProject("MyProject", "MyGrid")
    openProject = App.ActivateProject("PYTHON_TEST")
    project = App.GetActiveProject()
    projectName = project.loc_name

    #retrieve load-flow object
    ldf = App.GetFromStudyCase("ComLdf")

    #force balanced load flow
    ldf.iopt_net = 0

    #execute load flow
    ldf.Execute()

    print(projectName)

    #collect all relevant terminals
    App.PrintInfo("Collecting all calculation relevant terminals..")
    terminals = App.GetCalcRelevantObjects("*.ElmTerm")
    if not terminals:
        raise Exception("No calculation relevant terminals found")
    App.PrintPlain("Number of terminals found: %d" % len(terminals))

    for terminal in terminals:
        voltage = terminal.GetAttribute("m:u")
        App.PrintPlain("Voltage at terminal %s is %f p.u." % (terminal , voltage))
        print("Voltage at terminal " + terminal.loc_name + " is " + str(voltage)  + " p.u.")    #Es necesario casting para imprimir
    #print to PowerFactory output window
    App.PrintInfo("Python Script ended.")

#powerfactory.__version__

except pf.ExitError as error:
    print(error)
    print('error.code  = %d' % error.code)






#ejemplo generales
    #user = app.GetCurrentUser()
    #project = app.GetActiveProject()
    #script = app.GetCurrentScript()
    #objects = app.GetCalcRelevantObjects()
    #lines = app.GetCalcRelevantObjects("*.ElmLne")
    #sel = app.GetDiagramSelection()
    #sel = app.GetBrowserSelection()
    #project = app.CreateProject("MyProject", "MyGrid")
    #ldf = app.GetFromStudyCase("ComLdf")


# Acceso atributos
    #project = app.GetActiveProject()
    #projectName = project.loc_name
    #project.Deactivate()

    #lines = app.GetCalcRelevantObjects("*.ElmLne")
    #line = lines[0]
    #currLoading = line.GetAttribute("c:loading")

#Printing in PF
    #app.PrintPlain("Hello world!")
    #app.PrintInfo("An info!")
    #app.PrintWarn("A warning!")
    #app.PrintError("An error!")
