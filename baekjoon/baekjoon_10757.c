#include <stdio.h>
#include <string.h>

int main(void) {
	char str1[10001] = {0};
	char str2[10001] = {0};
	char ans[10002] = {0};
	int length = 0;
	int tmp = 0;
	int i = 0;
	
	scanf("%s %s", str1, str2);
	int len1 = strlen(str1);
	int len2 = strlen(str2);
	for (i = 0; i < len1; i++) {
		str1[i] = str1[i] - '0';
	}
	for (i = 0; i < len1 / 2; i++) {
		tmp = str1[i];
		str1[i] = str1[len1 - i - 1];
		str1[len1 - i - 1] = tmp;
	}
	for (i = 0; i < len2; i++) {
		str2[i] = str2[i] - '0';
	}
	for (i = 0; i < len2 / 2; i++) {
		tmp = str2[i];
		str2[i] = str2[len2 - i - 1];
		str2[len2 - i - 1] = tmp;
	}
	
	if (len1 > len2) {
		length = len1;	
	} else {
		length = len2;
	}
	
	for (i = 0; i < length; i++) {
		tmp = str1[i] + str2[i];
		if(tmp + ans[i] >= 10) {
			ans[i+1] = ans[i+1] + 1;
			ans[i] = tmp + ans[i] - 10;
		}
		else {
			ans[i] = ans[i] + tmp;
		}
	}
	for (i = length; i >= 0; i--) {
		if(i == length) {
			if(ans[i] == 0) {
				continue;
			}
		}
		printf("%d", ans[i]);
	}
}
