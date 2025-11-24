# Mobile UI Analyzer

**Analyze and optimize mobile UI/UX patterns for iOS and Android applications.**

**IMPORTANT: Ensure mobile interfaces follow platform guidelines and best practices.**

---

╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            SENA 🦁 MOBILE UI ANALYZER v3.3                           ║
║        iOS · Android · Material Design · Human Interface             ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════════════
  MOBILE UI ANALYSIS
════════════════════════════════════════════════════════════════════════

**Platform Compliance Score:**

┌────────────────────────────────────────────────────────────────────┐
│ Platform               │ Score  │ Guidelines │ Status             │
├────────────────────────────────────────────────────────────────────┤
│ iOS (HIG)              │ 72%    │ 156/217    │ ⚠️ Needs Work      │
│ Android (Material)     │ 68%    │ 143/210    │ ⚠️ Needs Work      │
│ Cross-Platform         │ 45%    │ Mixed      │ 🔴 Inconsistent    │
│ Accessibility          │ 56%    │ WCAG       │ ⚠️ Improve         │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  PLATFORM-SPECIFIC VIOLATIONS
════════════════════════════════════════════════════════════════════════

**iOS Human Interface Guidelines:**

┌────────────────────────────────────────────────────────────────────┐
│ Violation              │ Count │ Severity │ Fix                    │
├────────────────────────────────────────────────────────────────────┤
│ Back button custom     │ 12    │ 🔴 HIGH  │ Use system back        │
│ Tab bar > 5 items      │ 1     │ ⚠️ MED   │ Use "More" tab         │
│ Non-native alerts      │ 8     │ 🔴 HIGH  │ Use UIAlertController  │
│ Android FAB on iOS     │ 3     │ 🔴 HIGH  │ Remove or redesign     │
│ Small touch targets    │ 23    │ 🔴 HIGH  │ Min 44×44 pts          │
└────────────────────────────────────────────────────────────────────┘

**Android Material Design:**

┌────────────────────────────────────────────────────────────────────┐
│ Violation              │ Count │ Severity │ Fix                    │
├────────────────────────────────────────────────────────────────────┤
│ iOS navigation bar     │ 5     │ 🔴 HIGH  │ Use Material AppBar    │
│ Missing FAB            │ 12    │ ⚠️ MED   │ Add primary action     │
│ Wrong elevation        │ 34    │ ⚠️ MED   │ Follow elevation spec  │
│ iOS switches           │ 8     │ 🔴 HIGH  │ Use Material switches  │
│ Non-Material ripples   │ 45    │ 🟡 LOW   │ Add ripple effect      │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  RESPONSIVE LAYOUTS
════════════════════════════════════════════════════════════════════════

**Device Coverage:**

```
Screen Size Distribution:
Small   (320-375px)  ████████░░░░░░░░ 45%
Medium  (376-414px)  ██████░░░░░░░░░░ 35%
Large   (415-480px)  ███░░░░░░░░░░░░░ 15%
XLarge  (481px+)     █░░░░░░░░░░░░░░░  5%
```

**Layout Issues by Screen Size:**

┌────────────────────────────────────────────────────────────────────┐
│ Device                 │ Issues │ Critical │ Example              │
├────────────────────────────────────────────────────────────────────┤
│ iPhone SE (375×667)    │ 23     │ 5        │ Text truncation      │
│ iPhone 14 Pro (393×852)│ 12     │ 2        │ Bottom safe area     │
│ Pixel 5 (393×851)      │ 15     │ 3        │ Status bar overlap   │
│ Galaxy S21 (384×854)   │ 18     │ 4        │ Navigation gestures  │
│ iPad Mini (744×1133)   │ 34     │ 8        │ Poor tablet layout   │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  NAVIGATION PATTERNS
════════════════════════════════════════════════════════════════════════

**Current vs Recommended:**

```typescript
// ❌ CURRENT - Inconsistent navigation
const Navigation = () => {
  if (Platform.OS === 'ios') {
    return <CustomTabBar />; // Non-native
  } else {
    return <DrawerNavigation />; // Different on Android
  }
};

// ✅ RECOMMENDED - Platform-specific native patterns
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createMaterialBottomTabNavigator } from '@react-navigation/material-bottom-tabs';

const Tab = Platform.select({
  ios: createBottomTabNavigator(),
  android: createMaterialBottomTabNavigator(),
});

// Platform-specific styling
const screenOptions = {
  tabBarStyle: Platform.select({
    ios: {
      backgroundColor: 'white',
      borderTopWidth: StyleSheet.hairlineWidth,
    },
    android: {
      backgroundColor: '#6200EE',
      elevation: 8,
    },
  }),
};
```

════════════════════════════════════════════════════════════════════════
  GESTURE HANDLING
════════════════════════════════════════════════════════════════════════

**Touch & Gesture Analysis:**

┌────────────────────────────────────────────────────────────────────┐
│ Gesture Type           │ iOS    │ Android │ Implementation      │
├────────────────────────────────────────────────────────────────────┤
│ Swipe to dismiss       │ ✅     │ ❌      │ Missing on Android  │
│ Pull to refresh        │ ✅     │ ✅      │ Different styles    │
│ Long press actions     │ ⚠️     │ ✅      │ iOS needs haptic    │
│ Pinch to zoom          │ ✅     │ ✅      │ Consistent          │
│ Edge swipe (back)      │ ✅     │ ⚠️      │ Android fragmented  │
└────────────────────────────────────────────────────────────────────┘

**Gesture Implementation:**

```typescript
// ✅ Cross-platform gesture handling
import {
  GestureHandlerRootView,
  PanGestureHandler,
  State,
} from 'react-native-gesture-handler';

const SwipeableCard = () => {
  const translateX = useSharedValue(0);

  const gestureHandler = useAnimatedGestureHandler({
    onActive: (event) => {
      translateX.value = event.translationX;
    },
    onEnd: () => {
      translateX.value = withSpring(0);
    },
  });

  const animatedStyle = useAnimatedStyle(() => ({
    transform: [{ translateX: translateX.value }],
  }));

  return (
    <PanGestureHandler onGestureEvent={gestureHandler}>
      <Animated.View style={animatedStyle}>
        <Card />
      </Animated.View>
    </PanGestureHandler>
  );
};
```

════════════════════════════════════════════════════════════════════════
  COMPONENT PATTERNS
════════════════════════════════════════════════════════════════════════

**Platform-Specific Components:**

```typescript
// ✅ Platform-aware component library
const Button = ({ title, onPress, variant = 'primary' }) => {
  if (Platform.OS === 'ios') {
    return (
      <TouchableOpacity
        onPress={onPress}
        style={[styles.iosButton, styles[variant]]}
        activeOpacity={0.7}
      >
        <Text style={styles.iosButtonText}>{title}</Text>
      </TouchableOpacity>
    );
  }

  // Android Material Button
  return (
    <Pressable
      onPress={onPress}
      style={({ pressed }) => [
        styles.androidButton,
        styles[variant],
        pressed && styles.androidPressed,
      ]}
      android_ripple={{ color: 'rgba(0,0,0,0.12)' }}
    >
      <Text style={styles.androidButtonText}>{title}</Text>
    </Pressable>
  );
};

// ✅ Safe area handling
import { SafeAreaProvider, SafeAreaView } from 'react-native-safe-area-context';

const Screen = ({ children }) => (
  <SafeAreaView style={styles.container} edges={['top', 'bottom']}>
    {children}
  </SafeAreaView>
);

// ✅ Platform-specific styling
const styles = StyleSheet.create({
  container: {
    flex: 1,
    ...Platform.select({
      ios: {
        backgroundColor: '#F2F2F7', // iOS system background
      },
      android: {
        backgroundColor: '#FFFFFF',
      },
    }),
  },
  shadow: Platform.select({
    ios: {
      shadowColor: '#000',
      shadowOffset: { width: 0, height: 2 },
      shadowOpacity: 0.1,
      shadowRadius: 4,
    },
    android: {
      elevation: 4,
    },
  }),
});
```

════════════════════════════════════════════════════════════════════════
  PERFORMANCE METRICS
════════════════════════════════════════════════════════════════════════

**UI Performance:**

┌────────────────────────────────────────────────────────────────────┐
│ Metric                 │ iOS    │ Android │ Target  │ Status      │
├────────────────────────────────────────────────────────────────────┤
│ FPS (average)          │ 58     │ 52      │ 60      │ ⚠️ Close    │
│ JS Thread              │ 82%    │ 89%     │ < 80%   │ 🔴 High     │
│ UI Thread              │ 45%    │ 67%     │ < 60%   │ ⚠️ Android  │
│ Launch Time            │ 1.2s   │ 2.3s    │ < 1s    │ 🔴 Slow     │
│ Memory Usage           │ 123MB  │ 189MB   │ < 150MB │ ⚠️ Android  │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  ACCESSIBILITY MOBILE
════════════════════════════════════════════════════════════════════════

**Screen Reader Support:**

┌────────────────────────────────────────────────────────────────────┐
│ Feature                │ VoiceOver│ TalkBack│ Implementation     │
├────────────────────────────────────────────────────────────────────┤
│ Labels                 │ 67%     │ 62%     │ ⚠️ Missing labels   │
│ Hints                  │ 23%     │ 19%     │ 🔴 Very few         │
│ Traits/Roles           │ 45%     │ 41%     │ ⚠️ Incomplete       │
│ Actions                │ 34%     │ 31%     │ 🔴 Not announced    │
│ Live Regions           │ 12%     │ 8%      │ 🔴 Critical         │
└────────────────────────────────────────────────────────────────────┘

```typescript
// ✅ Accessible mobile components
<TouchableOpacity
  accessible={true}
  accessibilityLabel="Submit form"
  accessibilityHint="Double tap to submit your information"
  accessibilityRole="button"
  accessibilityState={{ disabled: isLoading }}
  onPress={handleSubmit}
>
  <Text>Submit</Text>
</TouchableOpacity>
```

════════════════════════════════════════════════════════════════════════
  OPTIMIZATION RECOMMENDATIONS
════════════════════════════════════════════════════════════════════════

**🔴 CRITICAL:**
1. Fix 23 small touch targets (< 44×44 pts)
2. Implement platform-specific navigation
3. Add safe area handling for all screens
4. Fix custom back buttons on iOS
5. Remove Android FAB from iOS version

**⚠️ HIGH:**
6. Optimize JS thread usage (reduce to < 80%)
7. Implement proper gesture handling
8. Add platform-specific animations
9. Fix screen reader labels
10. Reduce Android memory usage

**🟡 MEDIUM:**
11. Implement haptic feedback (iOS)
12. Add Material ripple effects (Android)
13. Optimize launch time
14. Add tablet-specific layouts
15. Implement dark mode support

════════════════════════════════════════════════════════════════════════
  COMMANDS
════════════════════════════════════════════════════════════════════════

• `/mobile-ui` - Full mobile UI analysis
• `/mobile-ui --ios` - iOS HIG compliance check
• `/mobile-ui --android` - Material Design check
• `/mobile-ui --gestures` - Gesture implementation
• `/mobile-ui --performance` - UI performance metrics
• `/mobile-ui --accessibility` - Mobile a11y audit

════════════════════════════════════════════════════════════════════════

**SENA 🦁 Mobile UI** - Native feel on every platform