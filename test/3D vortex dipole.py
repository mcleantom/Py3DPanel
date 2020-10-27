import numpy as np

def quadrilateral_u(sigma, y1, y2, y3, y4, r1, r2, r3, r4, d12, d23, d34, d41):
    """
    """
    strength_term = sigma/(4*np.pi)
    first = ((y2-y1)/d12) * np.log((r1+r2-d12)/(r1+r2+d12))
    second = ((y3-y2)/d23) * np.log((r2+r3-d23)/(r2+r3+d23))
    third = ((y4-y3)/d34) * np.log((r4+r3-d34)/(r4+r3+d34))
    fourth = ((y1-y4)/d41) * np.log((r4+r1-d41)/(r4+r1+d41))
    return strength_term*(first*second*third*fourth)

def quadrilateral_v(sigma, x1, x2, x3, x4, r1, r2, r3, r4, d12, d23, d34, d41):
    """
    """
    strength_term = sigma/(4*np.pi)
    first = ((x2-x1)/d12) * np.log((r1+r2-d12)/(r1+r2+d12))
    second = ((x3-x2)/d23) * np.log((r2+r3-d23)/(r2+r3+d23))
    third = ((x4-x3)/d34) * np.log((r4+r3-d34)/(r4+r3+d34))
    fourth = ((x1-x4)/d41) * np.log((r4+r1-d41)/(r4+r1+d41))
    return strength_term*(first*second*third*fourth)

def quadrilateral_w(z, sigma, m12, m23, m34, m41, e1, e2, e3, e4, h1, h2, h3, h4, r1, r2, r3, r4):
    """
    """
    strength_term = sigma/(4*np.pi)
    tan1 = np.arctan((m12*e1-h1)/(z*r1))
    tan2 = np.arctan((m12*e2-h2)/(z*r2))
    tan3 = np.arctan((m23*e2-h2)/(z*r2))
    tan4 = np.arctan((m23*e3-h3)/(z*r3))
    tan5 = np.arctan((m34*e3-h3)/(z*r3))
    tan6 = np.arctan((m34*e4-h4)/(z*r4))
    tan7 = np.arctan((m41*e4-h4)/(z*r4))
    tan8 = np.arctan((m41*e1-h1)/(z*r1))
    return strength_term(tan1-tan2+tan3-tan4+tan5-tan6+tan7-tan8)

def calc_d_terms(x1, x2, x3, x4, y1, y2, y3, y4):
    """
    """
    d12 = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    d23 = np.sqrt((x3-x2)**2 + (y3-y2)**2)
    d34 = np.sqrt((x4-x3)**2 + (y4-y3)**2)
    d41 = np.sqrt((x1-x4)**2 + (y1-y4)**2)
    return d12, d23, d34, d41

def calc_m_terms(x1, x2, x3, x4, y1, y2, y3, y4):
    """
    """
    m12 = (y2-y1)/(x2-x1)
    m23 = (y3-y2)/(x3-x2)
    m34 = (y4-y3)/(x4-x3)
    m41 = (y1-y4)/(x1-x4)
    return m12, m23, m34, m41

def calc_rk(x, xk, y, yk, z):
    return np.sqrt((x-xk)**2 + (y-yk)**2 + z**2)

def calc_ek(x, xk, z):
    return (x-xk)**2 + z**2

def calc_hk(x, xk, y, yk):
    return (x-xk)*(y-yk)

def calc_r_e_k_terms(xk, yk, x, y, z):
    """
    """
    r = []
    e = []
    h = []
    for xx, yy in zip(xk, yk):
        r.append(calc_rk(x, xx, y, yy, z))
        e.append(calc_ek(x, xx, z))
        h.append(calc_hk(x, xx, y, yy))
    return r, e, h

xc = np.array([1,10,10,1])
yc = np.array([1,0,10,1])
# xp = np.array([0,1])
# yp = np.array([0,1])
# zp = np.array([0,1])
# r, e, hk = calc_r_e_k_terms(xc, yc, xp, yp, zp)

nx, ny, nz = (10, 10, 10)
xl = np.linspace(-5, 5, nx)
yl = np.linspace(-5, 5, ny)
zl = np.linspace(-5, 5, nz)
xv, yv, zv = np.meshgrid(xl, yl, zl)

r, e, hk = calc_r_e_k_terms(xc, yc, xv, yv, zv)
d = calc_d_terms(xc[0], xc[1], xc[2], xc[3], yc[0], yc[1], yc[2], yc[3])
m = calc_m_terms(xc[0], xc[1], xc[2], xc[3], yc[0], yc[1], yc[2], yc[3])

sigma = 1

u = quadrilateral_u(sigma, yc[0], yc[1], yc[2], yc[3], r[0], r[1], r[2], r[3], d[0], d[1], d[2], d[3])