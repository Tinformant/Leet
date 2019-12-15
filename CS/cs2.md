# Computer Set 2 Code
## Problem 1
### Part 1
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
Test code:
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
```
### Part 2
Test code:
```matlab
clear;
tic
filename = '/Users/jarvis_Mac/Desktop/Data/EE104/Homework/cs02s218/pic/p1_2.png';
% m is the same m in the problem statement, f means equally divide the probability
% 0.1-0.9 into f parts, T denotes the threshold when H < 0.05, p is
% different probability

m = 50; n = 1; f = 5;
[p, Tmean, Terr] = p1_2(m,f,n);

f = figure;
errorbar(p,Tmean,Terr)
xlabel('Probability P');
ylabel('N of Threshold');
title('Threshold N vs Different probability');

saveas(f,filename);
```
For 20 Monte Carlo trials with p from 0.1 to 0.9:
```matlab
function [k, Tmean, Terr] = p1_2(m,f,n)
% prabability from 0.1 to 0.9, repeat 20 times Monte Carlo
    k = zeros(f,1);
    T = zeros(f,20);
    for j = 1:20
       for i = 1:f
            p = i*0.8/(f-1)-0.1;
            k(i,1) = p;
            T(i,j) = get_T(m,p,n);   
       end
       Tmean = mean(T,2); 
       Terr = std(T,0,2);
       t1 = toc;
       fprintf('interval = %8.5f\n',t1);
       tic
    end
end
```
For threshold T to make the Hellinger distance < 0.05:
```matlab
function [T,H] = get_T(m,p,n) 
% get Threshold of the N, while H < 0.05
    N = 100;
    H = 1;
    while (H > 0.05)
        H = get_H(m,p,N,n);
        N = N + 5;
    end
    T = N;
end
```
### Part 3
Cost function:
```matlab
function [C,cstd] = get_C(m,p,N,n)
% get the cost function
    [H,h] = get_H(m,p,N,n);
    C = 6e-4*N + H;
    c = 6e-4*N + h;
    cstd = std(c);
end
```

## Problem 2
Test code:
```matlab
N = 100000;
p1 = BerGenerator(N,0.3);
p2 = BerGenerator(N,0.4);
p3 = BerGenerator(N,0.6);
[p,W] = func(p1,p2,p3);
```
```matlab
function [a,p] = BerGenerator(N,p0)
% generate a column of N random 0 1 series with the probablity of P(x=1)=p0
    p = 0;
    if p0>1
        fprintf("Watch out you probability!!\n");
    elseif p0<0
        fprintf("Watch out you probability!!\n"); 
    else
        a = rand(1,N);
        for i=1:N
            if a(1,i) <= p0 
                a(1,i) = 1;
                p = p+1;
            else
                a(1,i) = 0;
            end
        end
        a = a';
        p = p/N;
    end
end
```
