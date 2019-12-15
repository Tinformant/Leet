Generate a binomial PMF with the probability of p0: 
```matlab
function [S,x] = generateSample(m,p,N,n)
% generate a PMF of binomial variable 
    R = binornd(m,p,N,n);
    S = zeros(m+1,1);
    for i = 1:n
        x = tabulate(R(:,i));
        S(x(:,1)+1,i) = x(:,2)/N;
    end
end
```
This one is the function of calculatingn the Hellinger Distance.
```matlab
function [H,h,R,Theo] = get_H(m,p,N,n)
% get the Hellinger distance 
    R = generateSample(m,p,N,n);  
    Theo = (binopdf(0:1:m,m,p))';
    h = 1/sqrt(2)*sqrt(sum((sqrt(R)-sqrt(Theo)).^2));
    H = mean(h);
end
```
Test code for 1-1:
```matlab
% problem_1_3
clear;
tic
filename = '/Users/jarvis_Mac/Desktop/Data/EE104/Homework/cs02s218/pic/p1_1.png';
% H is Hellinger Distance of the practical result and theoretical result; R
% is the simulation of the binomial distribution

t = (0:1:10)';
m = 10; p = 1/2; N = 100; n = 1;
[H,h,R,Theo] = get_H(m,p,N,n);

f = figure;
plot(t,R,t,Theo)
xlabel('m : Numbers of Xi has the value 1');
ylabel('P: Probability');
title('Practical and Theoretical  Binomial Distriubution');
legend("Practical","Theoretical")

saveas(f, filename);
```matlab
