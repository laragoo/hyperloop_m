% c_p = specific heat at constant pressure
% c_v = specific heat at constant volume
% http://www.engineeringtoolbox.com/moody-diagram-d_618.html
% TODO: alter to diagram

% [dimensionless]
function gamma = adiabaticGasConst(c_p, c_v)
gamma = c_p / c_v;
