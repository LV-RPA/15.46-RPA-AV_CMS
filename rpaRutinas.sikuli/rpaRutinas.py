import datetime
import os 
import glob

desde = datetime.datetime.now()
hasta = datetime.datetime.now()
user_cms = ("CQUISP65")
pass_cms = ("Claudio02202")
user_inguz = ("74590179")
pass_inguz = ("jarvis")
link_inguz = ("www.anovo.pe/inguz")
link_carga = ("http://www.anovo.pe/inguz/formRutinas/frmCargarOrdenes.aspx")
ruta = (r'\\10.120.15.46\Rutinas')
delete_files = (r'\\10.120.15.46\Rutinas\*')
print(desde)
print(hasta)

print("cerrar procesos")
os.system('taskkill /f /im cms.exe')
os.system('taskkill /f /im te_envot.exe')
os.system('taskkill /f /im te_alav.exe')
os.system('taskkill /f /im te_manot.exe')
os.system('taskkill /f /im te_rreot.exe')
os.system('taskkill /f /im firefox.exe')

print("Eliminar Archivos")
files = glob.glob(delete_files) 
for f in files:
    os.remove(f)

print("Abrir CMS")
App.open("C:\\Gescab\\cms.exe")
sleep(5)

print("Esperar CMS")
wait(Pattern("1557418414969.png").similar(0.80),1800)
sleep(2)
paste("1557418673300.png", user_cms)
sleep(2)
type(Key.TAB)
sleep(2)
paste(pass_cms)
sleep(2)
type(Key.ENTER)
sleep(2)
wait(Pattern("1555191558075.png").similar(0.80),240)
sleep(2)
click("1555191572231.png")
sleep(2)
click("1555191587121.png")
sleep(2)
click(Pattern("1555191605081.png").targetOffset(6,11))
sleep(2)
click("1555191630786.png")
sleep(2)
wait(Pattern("1555191646245.png").similar(0.80),240)
sleep(2)

print("listo, cable mágico")
def cambiarusuario():
    type("u",KEY_ALT)
    sleep(1)
    type("s",KEY_ALT)
    sleep(1)

cambiarusuario()
cambiarusuario()
cambiarusuario()
cambiarusuario()
cambiarusuario()
sleep(10)

print("buscar modulo")
doubleClick(Pattern("1555191664304.png").targetOffset(-68,2))
sleep(10)
click(Pattern("1555191664304.png").targetOffset(-68,2))
sleep(2)
wait("1555191780299.png")
sleep(2)
print("salio en proceso")
click(Pattern("1555191795518.png").targetOffset(-59,0))
sleep(2)
click(Pattern("1557247089245.png").targetOffset(-100,2))
sleep(2)
print("Inicio exportar Rutinas")
doubleClick(Pattern("1557247252348.png").targetOffset(-7,0))
sleep(2)
wait(Pattern(Pattern("1559245120921.png").targetOffset(-35,2)).similar(0.8),3600)
sleep(2)

print("Comenzamos con el modulo de exportar rutinas")
click(Pattern("1559245120921.png").targetOffset(29,2))
sleep(2)
type(Pattern("1557247925243-1.png").targetOffset(23,1), desde.strftime("%d%m%Y"))
sleep(2)
type(Pattern("1557247947710-1.png").targetOffset(22,2), hasta.strftime("%d%m%Y"))
sleep(2)
print("quitamos los materiales")
click(Pattern("1557248029497.png").targetOffset(-31,0))
sleep(2)
print("Seleccionamos la ofincia(Lima)")
doubleClick(Pattern("1557248107704.png").targetOffset(68,35))
click(Pattern("1557248137774.png").targetOffset(20,1))
click(Pattern("1557248228172.png").targetOffset(-53,18))
sleep(2)
print("Guardar el archivo rutinas")
click(Pattern("1557249144725.png").targetOffset(0,2))
sleep(3)
click(Pattern("1567036305220.png").targetOffset(1,-8))
sleep(2)
click(Pattern("1567036353265.png").targetOffset(121,1))
sleep(2)
print("selecciona la carpeta")
click(Pattern("1557249231627.png").targetOffset(-10,0))
sleep(2)
click(Pattern("1557260485379.png").targetOffset(-17,1))
sleep(2)
click(Pattern("1555257275331.png").targetOffset(-16,15))
print("Guardar archivo envio_ot")
type(Pattern("1557255184146.png").targetOffset(19,0), "envio_ot")
sleep(2)
type(Key.ENTER)
sleep(5)
print("Cerrar exportar envio_ot")
wait(Pattern(Pattern("1559276778469.png").targetOffset(23,35)).similar(0.8),3600)
sleep(2)
click(Pattern("1559276778469.png").targetOffset(23,35))
sleep(2)
click(Pattern("1559276818342.png").targetOffset(2,4))

print("exportar resumen ot")
sleep(2)
click(Pattern("1557259912522.png").targetOffset(-55,0))
sleep(2)
click(Pattern("1557259967821.png").targetOffset(-54,2))
sleep(2)
click(Pattern("1557260014775.png").targetOffset(-82,1))
sleep(2)
doubleClick(Pattern("1557260123996.png").targetOffset(-9,1))
sleep(2)
wait(Pattern("1560963187841.png").similar(0.80),3600)
sleep(2)
click(Pattern("1560963187841.png").targetOffset(-25,14))
sleep(2)
type(Pattern("1557261293378.png").targetOffset(55,-10), desde.strftime("%d%m%Y"))
sleep(2)
type(Pattern("1557261293378.png").targetOffset(55,36), hasta.strftime("%d%m%Y"))
click(Pattern("1557262127818.png").targetOffset(-37,1))
sleep(2)

print("Seleccionar el estado")
click("1557262095301.png")
sleep(2)

print("seleccionar contrata")
click(Pattern("1557262192800-1.png").targetOffset(19,11))
sleep(2)

for step in range(12):
    click(Pattern("1557262911189.png").targetOffset(-30,27))
    sleep(1)

print("Seleccionar contrata")
click("1557263057037.png")
sleep(2)

print("Listo para exportar")
click("1557263165457.png")
wait(Pattern("1557263589943.png").similar(0.80),3600)
sleep(2)
click(Pattern("1567037487013.png").targetOffset(1,-10))
sleep(2)
click(Pattern("1567037515329.png").targetOffset(124,0))
sleep(2)
click(Pattern("1567037550036.png").targetOffset(-90,0))
sleep(3)
type(Pattern("1557263804148.png").targetOffset(32,-2), "resumen_ot")
sleep(2)
click("1557263865702.png")

print("Guardar archivo Resumen OT")
sleep(2)
wait(Pattern(Pattern("1557264120972-1.png").targetOffset(87,55)).similar(0.8),3600)
sleep(2)
click(Pattern("1557264120972.png").targetOffset(87,55))
sleep(2)
click("1557876053934.png")
sleep(3)

print("Inicio exportar Averias OT")
doubleClick(Pattern("1557270769684-1.png").targetOffset(2,1))
wait(Pattern("1560963187841-1.png").similar(0.80),3600)
sleep(2)
click(Pattern("1560963187841-1.png").targetOffset(-25,14))
sleep(2)
type(Pattern("1557261293378-1.png").targetOffset(55,-10), desde.strftime("%d%m%Y"))
sleep(2)
type(Pattern("1557261293378-1.png").targetOffset(55,36), hasta.strftime("%d%m%Y"))
sleep(2)
click(Pattern("1557271115653-1.png").targetOffset(-42,-1))
sleep(2)

print("Seleccionar el estado de averias")
click("1557262095301-1.png")
sleep(2)

print("seleccionar contrata")
click(Pattern("1557262192800-2.png").targetOffset(19,11))
sleep(2)

for step in range(19):
    click(Pattern("1557262911189-1.png").targetOffset(-30,27))
    sleep(1)

print("Seleccionar contrata 333 para averias")
click("1557263057037-1.png")
sleep(2)

print("Listo para exportar averias")
click("1557263165457-1.png")
sleep(2)
wait(Pattern("1557263589943-1.png").similar(0.80),3600)
sleep(2)
click(Pattern("1567037487013-1.png").targetOffset(1,-10))
sleep(2)
click(Pattern("1567037515329-1.png").targetOffset(124,0))
sleep(2)
click(Pattern("1567037550036-1.png").targetOffset(-90,0))
sleep(3)
type(Pattern("1557263804148-1.png").targetOffset(32,-2), "pendiente_averias")
sleep(2)
click("1557263865702-1.png")

print("Guardar archivo Pendiente Averias")
sleep(2)
wait(Pattern(Pattern("1557264120972-1.png").targetOffset(87,55)).similar(0.8),640)
sleep(2)
click(Pattern("1557264120972.png").targetOffset(87,55))
sleep(2)
click("1557876306233.png")
sleep(2)

print("cerrar CMS")
click(Pattern("1555389366717-2.png").targetOffset(110,2))
wait(Pattern("1555389401450-2.png").similar(0.80),240)
sleep(2)
click(Pattern("1555389401450-2.png").targetOffset(25,52))
sleep(5)

#*********************ABRIR FIREFOX********************#
print("abrir Firefox")
App.open("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
sleep(15)

print("Nos logueamos")
paste(user_inguz)
sleep(5)
type(Key.TAB)
sleep(5)
paste(pass_inguz)
sleep(5)
type(Key.ENTER)
sleep(3)
wait("1571942741051-1.png",120)
sleep(2)

print("ingresar el link de carga")
type("l",KEY_CTRL)
sleep(2)
paste(link_carga)
sleep(2)
type(Key.ENTER)

print("listo - Modulo de carga")
sleep(15)
click("1557348730358-5.png")
sleep(2)
click(Pattern("1559244554264-2.png").targetOffset(-33,17))
sleep(3)
type("l",KEY_CTRL)
sleep(2)
paste(ruta)
sleep(2)
type(Key.ENTER)
sleep(3)

print("comenzamos a seleccionar los archivos")
click("1557352254606-6.png")
sleep(2)
click("1557586606005-5.png")
sleep(3)
click(Pattern("1569686810015.png").targetOffset(-146,30))

print("Encontramos la ruta envio_ot_lim")
sleep(3)
click("1557352278020-5.png")
sleep(2)
click("1557586606005-5.png")
sleep(3)
click(Pattern("1569687043714.png").targetOffset(-144,-59))

print("Encontramos la ruta envio_ot_lim_det")
sleep(3)
click("1557352083255-5.png")
sleep(2)
type(Key.ENTER)
sleep(3)

print("Listo para importar en el INGUZ")
click(Pattern("1559244690937-2.png").targetOffset(4,2))
sleep(2)
wait(Pattern("1560193987932.png").similar(0.80),600)
sleep(2)

print("listo")
type("l",KEY_CTRL)
sleep(2)
paste(link_carga)
sleep(1)
type(Key.ENTER)
sleep(10)
click(Pattern("1559275550170-1.png").targetOffset(34,1))
sleep(3)
click(Pattern("1559244725938-2.png").targetOffset(-54,17))
sleep(2)
click(Pattern("1559076190450-3.png").targetOffset(-35,0))
sleep(2)
type(Key.ENTER)
sleep(2)
click(Pattern("1559244755557-2.png").targetOffset(6,2))
sleep(2)
wait(Pattern("1560194024555.png").similar(0.80),600)

print("fin del RPA rutinas")
sleep(3)
type("w",KEY_CTRL)
sleep(2)