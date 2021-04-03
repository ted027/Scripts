function J = costFunctionJ(X, y, theta)

% X is the design matrix, training examples
% y is the class labels

m = size(X, 1); % num of traiing data
predictions = X*theta; % predictions of hypothesis on all m examples
sqrErrors = (predictions-y).^2; % squared sqrErrors 

J = 1/(2*m) * sum(sqrErrors);