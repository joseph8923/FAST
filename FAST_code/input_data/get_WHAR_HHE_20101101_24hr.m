function [t, x, Fs] = get_WHAR_HHE_20101101_24hr()

% Read in data from station WHAR, channel HHE, 20101101, 24 hours
path(path,'./MatSAC');
[t,x,SAChdr] = fget_sac('../data/GuyArkansas/201011_HHE_BP_1_1.SAC');
Fs = 100;

t = t(1:end-1);
x = x(1:end-1);

% Filter data 1-20 Hz, normalize (from Yihe's scripts)
[x] = filter_taper_guy_data(x, Fs);

end