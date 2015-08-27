
  def  rangex = np.linspace(0, 10, 100, endpoint=True)
 
print(midpoint.integrate(intf, rangex))
out = "{} integration, e^x on ({},{}): {}"

print(out.format(
    "midpoint",
    rangex[0], rangex[-1],
    midpoint.integrate(intf, rangex)
))

from scipy.integrate import quad

print(out.format(
    "scipy",
    rangex[0], rangex[-1],
   quad(intf, rangex[0], rangex[-1])))
