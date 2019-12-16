# Computer set 3 Code
## Problem 1
### Part 2
For approximating PDF:
```matlab
function [Result_pdf,Result_cdf,X] = P1(Data, Num_Bins, X_Max, X_Min)
    Bin_Size = (X_Max - X_Min)/Num_Bins;
    Edge = zeros(1,Num_Bins+1);
    Edge(1,Num_Bins+1) = X_Max;
    X = zeros(1,Num_Bins);
    for i = 1:Num_Bins
       Edge(1,i) = X_Min + (i-1)*Bin_Size;
       X(1,i) = X_Min + (i-0.5)*Bin_Size;
    end
    Result_pdf = histcounts(Data, Edge(1,:),'Normalization','pdf');
    Result_cdf = histcounts(Data, Edge(1,:),'Normalization','cdf');
end
```
### Part 3
```matlab
file1 = '/Users/sir/Desktop/Data/EE104/Homework/Guass.png';
file2 = '/Users/sir/Desktop/Data/EE104/Homework/Uni.png';
Num_Data = 10000;
Data_Norm = randn(Num_Data,1);
Data_Uni = 6*rand(Num_Data,1) - 1; 
X_Max = 7; X_Min = -7; Num_Bins = 100;
[rpdf,rcdf,x] = P1(Data_Norm, Num_Bins, X_Max, X_Min);
f1 = figure;
yyaxis left
ylabel('Probablity of PDF'); xlabel('Sample Value');
yyaxis right
ylabel('Probablity of CDF');
hold on;
yyaxis left
plot(x,rpdf,'LineWidth',2);
set(gca,'FontSize',12);
yyaxis right
plot(x,rcdf,'--o','LineWidth',1.5);
title({'PDF and CDF of 10000 Gaussian samples';' '}); legend('pdf','cdf');
[rpdf,rcdf,x] = P1(Data_Uni, Num_Bins, X_Max, X_Min);
f2 =figure;
yyaxis left
ylabel('Probablity of PDF'); xlabel('Sample Value');
yyaxis right
ylabel('Probablity of CDF');
hold on;
yyaxis left
plot(x,rpdf,'LineWidth',2); set(gca,'FontSize',12);
yyaxis right
plot(x,rcdf,'--o','LineWidth',1.5);
title({'PDF and CDF of 10000 Uniform samples';' '}); legend('pdf','cdf');
saveas(f1,file1); saveas(f2,file2);
```
## Problem 2
### Part 1
```matlab
function [D,S]= generateD(p,sigma2)
    sigma = sqrt(sigma2); N = normrnd(0,sigma); S = rand(1);
    if S<p
        S = 1;
    else
        S = 0;
    end
    D = S + N;    
end
```
### Part 2
Here is another function for calculating the probablity of PFA and PD: 
```matlab
function [Pd,Pfa] = detect(p,sigma2,eta,Num_Sample)
    Pd = 0; Pfa = 0; count = 0;
    for i = 1:Num_Sample
        [D,S] = generateD(p,sigma2);
        if S == 1
            count = count + 1;
        end 
        [D,S] = generateD(p,sigma2);
        if D > eta
            if S == 1
                Pd = Pd + 1;
            else 
                Pfa = Pfa + 1;
            end
        end 
    end
    Pd = Pd/Num_Sample; Pfa = Pfa/(Num_Sample-count);
```
