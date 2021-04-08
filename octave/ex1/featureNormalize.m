function [X_norm, mu, sigma] = featureNormalize(X)
%FEATURENORMALIZE Normalizes the features in X 
%   FEATURENORMALIZE(X) returns a normalized version of X where
%   the mean value of each feature is 0 and the standard deviation
%   is 1. This is often a good preprocessing step to do when
%   working with learning algorithms.

% You need to set these values correctly
X_norm = X;
mu = zeros(1, size(X, 2));
sigma = zeros(1, size(X, 2));

% ====================== YOUR CODE HERE ======================
% Instructions: First, for each feature dimension, compute the mean
%               of the feature and subtract it from the dataset,
%               storing the mean value in mu. Next, compute the 
%               standard deviation of each feature and divide
%               each feature by it's standard deviation, storing
%               the standard deviation in sigma. 
%
%               Note that X is a matrix where each column is a 
%               feature and each row is an example. You need 
%               to perform the normalization separately for 
%               each feature. 
%
% Hint: You might find the 'mean' and 'std' functions useful.
%       

feature1 = X(:,1);
feature2 = X(:,2);

mean1 = mean(feature1);
mean2 = mean(feature2);

mu = [mean1 mean2];
mu = [(feature1 - mean1) (feature2 - mean2)];

std1 = std(feature1);
std2 = std(feature2);
sigma = [std1 std2];

f1_norm = (feature1 - mean1) / std1;
f2_norm = (feature2 - mean2) / std2;

X_norm = [f1_norm f2_norm];

% ============================================================

end
