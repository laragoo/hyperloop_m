% Loads design parameters for hyperloop model
% McGill Hyperloop team

%% Tube
Tube.temp_ambient	= 293	% K
Tube.pressure_ambient	= 100	% Pa
%Tube.powerGridMax    = 6e6;	% max grid power is 6 MW (pg 35)
%Tube.powerSolar	     = 2.85e6;	% peak solar power (pg 35)
%Tube.energyStorage   = 36e6*60*60; % 36 Mwhr (pg 35) (W-s)

%% Pod
Pod.maxMass	     = 5000;	% kg
Pod.maxLength	     = 14;	% ft
Pod.maxBaseWidth     = 3.5;	% ft
Pod.maxWidth	     = 4.5;	% ft
Pod.maxHeight	     = 3.75;	% ft

%% Position within tube (x,y,z)

%% Acceleration within tube (x,y,z)

%% Vehicle attitude (roll, pitch, yaw)

%% Pod pressure

%% Temp from at least 2 pod points

%% Power consumption

%% Compressor
Comp.CoolantTemp     = 293;	% K
Comp.CoolantMass     = 290;	% kg
Comp.Comp1Ratio      = 21;
Comp.IC1OutletTemp   = 300;	% K
Comp.FlowtoSkiis     = 0.2;	% kg/sec
Comp.Comp2Ratio	     = 5.2;
Comp.IC2OutletTemp   = 400;	% K
