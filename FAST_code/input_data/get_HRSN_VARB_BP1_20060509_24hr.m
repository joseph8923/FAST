function [t, x, Fs] = get_HRSN_VARB_BP1_20060509_24hr()

% Read in data from HRSN, station VARB, channel BP1, 20060509, 24 hr
% Band pass 2-8 Hz
path(path,'./MatSAC');
[t, x, SAChdr] = fget_sac('../data/hrsn/2006.129.00.00.00.0336.BP.VARB..BP1.Q.SAC.bp2to8');
Fs = round(1.0 / SAChdr.times.delta); % sampling rate

end