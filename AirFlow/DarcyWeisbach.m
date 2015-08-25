% calculate friction losses resulting from fluid motion in pipes
% headLoss = head loss due to friction
% f_D = Darcy friction factor
% l = pipe length
% d = pipe diameter
% v = flow velocity
% g = gravitatioinal acceleration

% energy loss is dependent on wall shear stress (T) between fluid and pipe surface, which is also dependent on whether flow is turbulent or laminar
%	- turbulent: pressure drop is dependent on roughness of surface, as thin viscous layer is formed near pipe surface that causes energy loss
%	- laminar: rouchness effects are turbulent, as viscous layer is non-existant

function headLoss = DarcyWeisbach(f_D, l, d, v, g)
headLoss = f_D * (l/d) * ((v^2)/(2*g));
