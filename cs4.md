## Computer Set 4 Code
### Question 2
```matlab
Num_Data = 250000; 
I0 = 1; 
V0 = 1;
Data_R = rand(Num_Data,1) + 1;
Data_C = 3.5 * rand(Num_Data,1) + 1.5;
Data_L = exprnd(2,[Num_Data,1]) + 1;
Data_alpha = Data_R./(2.*Data_L);
Data_omega = 1./sqrt(Data_C.*Data_L);
Data = Data_alpha - Data_omega;
Data(Data<0)=0; 
Data(Data>0)=1; 
fprintf('the probability of overdamped system is %fnn', sum(Data)/Num_Data);
fprintf('the probability of underdamped system is %fnn', (Num_Data-sum(Data))/Num_Data);
```

### Question 3
```matlab
S1 = -Data_alpha(Data == 1) + sqrt(Data_alpha(Data == 1).^2 - Data_omega(Data == 1).^2);
S2 = -Data_alpha(Data == 1) - sqrt(Data_alpha(Data == 1).^2 - Data_omega(Data == 1).^2);

L = Data_L(Data == 1); 
R = Data_R(Data == 1); 
A = zeros(2,length(S1));

for i_t = 1:length(S1)
    A(:,i_t) = [1,1;S1(i_t,1),S2(i_t,1)]\[I0; -1/L(i_t,1)*(R(i_t,1)*I0+V0)];
end

A1 = A(:,1); 
A2 = A(:,2); 

[pS1,cS1,xS1] = pcdf(S1,50,max(S1)+0.1*(max(S1)-min(S1)),min(S1)-0.1*(max(S1)-min(S1)));
[pS2,cS2,xS2] = pcdf(S2,50,max(S2)+0.1*(max(S2)-min(S2)),min(S2)-0.1*(max(S2)-min(S2)));
[pA1,cA1,xA1] = pcdf(A1,50,0,-10);
[pA2,cA2,xA2] = pcdf(A2,50,10,0);

f(1,1) = figure;
yyaxis left; ylabel('Probablity Density Function'); xlabel('Sample Value');
yyaxis right; ylabel('Cumulative Density Function');
hold on;
yyaxis left; plot(xS1,pS1,'LineWidth',2); set(gca,'FontSize',12);
yyaxis right; plot(xS1,cS1,'--o','LineWidth',1.5);
title({'Given a overdamped system, margin PDF and CDF of S1';' '});legend('pdf','cdf','Location','northwest');

f(2,1) = figure;
yyaxis left; ylabel('Probablity Density Function'); xlabel('Sample Value');
yyaxis right; ylabel('Cumulative Density Function');
hold on;
yyaxis left; plot(xS2,pS2,'LineWidth',2); set(gca,'FontSize',12);
yyaxis right; plot(xS2,cS2,'--o','LineWidth',1.5);
title({'Given a overdamped system, margin PDF and CDF of S2';' '});legend('pdf','cdf','Location','northwest');

f(3,1) = figure;
yyaxis left; ylabel('Probablity Density Function'); xlabel('Sample Value');
yyaxis right; ylabel('Cumulative Density Function');
hold on;
yyaxis left; plot(xA1,pA1,'LineWidth',2); set(gca,'FontSize',12);
yyaxis right; plot(xA1,cA1,'--o','LineWidth',1.5);
title({'Given a overdamped system, margin PDF and CDF of A1';' '});legend('pdf','cdf','Location','northwest');

f(4,1) = figure;
yyaxis left; ylabel('Probablity Density Function'); xlabel('Sample Value');
yyaxis right; ylabel('Cumulative Density Function');
hold on;
yyaxis left; plot(xA2,pA2,'LineWidth',2); set(gca,'FontSize',12);
yyaxis right; plot(xA2,cA2,'--o','LineWidth',1.5);
title({'Given a overdamped system, margin PDF and CDF of A2';' '});legend('pdf','cdf','Location','northwest');
```
### Question 4
```matlab
omega_D = sqrt(Data_omega(Data == 0).^2 - Data_alpha(Data == 0).^2);
L2 = Data_L(Data == 0); R2 = Data_R(Data == 0); AA = zeros(2,length(omega_D));
alpha = Data_alpha(Data == 0);
for i_t = 1:length(omega_D)
    AA(:,i_t) = [1,0;-alpha(i_t,1),omega_D(i_t,1)]\[I0; -1/L2(i_t,1)*(R2(i_t,1)*I0+V0)];
end
AA = AA';
AA1 = AA(:,1); AA2 = AA(:,2); 

[pWd,cWd,xWd] = pcdf(omega_D,50,max(omega_D)+0.1*(max(omega_D)-min(omega_D)),
        min(omega_D)-0.1*(max(omega_D)-min(omega_D)));
[pAA1,cAA1,xAA1] = pcdf(AA1,100,2,0);
[pAA2,cAA2,xAA2] = pcdf(AA2,50,100,-100);

f(5,1) = figure;
yyaxis left; ylabel('Probablity Density Function'); xlabel('Sample Value');
yyaxis right; ylabel('Cumulative Density Function');
hold on;
yyaxis left; plot(xWd,pWd,'LineWidth',2); set(gca,'FontSize',12);
yyaxis right; plot(xWd,cWd,'--o','LineWidth',1.5);
title({'Given a underdamped system, margin PDF and CDF of \omega_d';' '});legend('pdf','cdf','Location','northwest');

f(6,1) = figure;
yyaxis left; ylabel('Probablity Density Function'); xlabel('Sample Value');
yyaxis right; ylabel('Cumulative Density Function');
hold on;
yyaxis left; plot(xAA1,pAA1,'LineWidth',2); set(gca,'FontSize',12);
yyaxis right; plot(xAA1,cAA1,'--o','LineWidth',1.5);
title({'Given a underdamped system, margin PDF and CDF of A1';' '});legend('pdf','cdf','Location','northwest');

f(7,1) = figure;
yyaxis left; ylabel('Probablity Density Function'); xlabel('Sample Value');
yyaxis right; ylabel('Cumulative Density Function');
hold on;
yyaxis left; plot(xAA2,pAA2,'LineWidth',2); set(gca,'FontSize',12);
yyaxis right; plot(xAA2,cAA2,'--o','LineWidth',1.5);
title({'Given a underdamped system, margin PDF and CDF of A2';' '});legend('pdf','cdf','Location','northwest');
```
### Question 5
For testing:
```matlab
% PDF of t = 1s
t = 1;
i_over = A1.*exp(S1*t) + A2.*exp(S2*t);
i_under = exp(-Data_alpha(Data == 0)*t).*(AA1.*cos(omega_D*t)+AA2.*sin(omega_D*t));
i_t = [i_over;i_under];
[pI,cI,xI] = pcdf(i_t,50,max(i_t)+0.1*(max(i_t)-min(i_t)),min(i_t)-0.1*(max(i_t)-min(i_t)));

f(8,1) = figure;
yyaxis left; ylabel('Probablity Density Function'); xlabel('Sample Value');
yyaxis right; ylabel('Cumulative Density Function');
hold on;
yyaxis left; plot(xI,pI,'LineWidth',2); set(gca,'FontSize',12);
yyaxis right; plot(xI,cI,'--o','LineWidth',1.5);
title({'Given t = 1s, PDF and CDF of i(s)';' '});legend('pdf','cdf','Location','northwest');
```
For simulating PDF and CDF:
```
function [Result_pdf,Result_cdf,X] = pcdf(Data, Num_Bins, X_Max, X_Min)
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
